from flask import render_template, flash, redirect, url_for, request, g
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from datetime import date
from app import db
from app.auth import bp
from app.auth.forms import LoginForm, RegistrationForm, ResetPasswordRequestForm, ResetPasswordForm
from app.models import User, Season
from app.auth.email import send_password_reset_email, send_verification_email

@bp.before_request
def before_request():
    g.all_seasons = Season.query.all()

@bp.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', 'danger')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not user.verified:
            return redirect(url_for('auth.unverified_email'))
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)
    return render_template('auth/login.html', title='Sign In', form=form)

@bp.route('/logout')
def logout():
    logout_user()
    flash('Logout successful!')
    return redirect(url_for('auth.login'))

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        #flash('Congratulations, you are now registered!')
        #return redirect(url_for('auth.login'))
        send_verification_email(user)
        return redirect(url_for('auth.unverified_email'))
    return render_template('auth/register.html', title='Register', form=form)


@bp.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Check your email for instructions to reset your password')
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_password_request.html', title='Reset Password', form=form)


@bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('main.index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_password.html', form=form)


@bp.route('/verify_email/<token>', methods=['GET', 'POST'])
def verify_email(token):

    user = User.verify_user_token(token, task='verify_email')
    if not user:
        flash('Email verification failed, please login to continue.', 'warning')
        logout_user()
        return redirect(url_for('auth.login'))

    if user.is_authenticated and user.verified:
        flash('Your account has already been verified.')
        return redirect(url_for('main.index'))

    user.verified = True
    user.verified_on = date.today()
    db.session.add(user)
    db.session.commit()
    flash('Thank you for verifying your account. Please login.')
    logout_user()
    return redirect(url_for('auth.login'))

@bp.route('/unverified_email', methods=['GET', 'POST'])
def unverified_email():
    if current_user.is_authenticated and current_user.verified:
        flash('Your account has already been verified.')
        return redirect(url_for('main.index'))

    return render_template('auth/unverified_email.html')


@bp.route('/resend_email_verification', methods=['GET', 'POST'])
@login_required
def resend_email_verification():
    print('resend')
    send_verification_email(current_user)
    flash('Verification email has been sent, please check your inbox.')
    return redirect(url_for('auth.unverified_email'))
