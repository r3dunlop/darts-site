from flask import render_template, flash, redirect, url_for, request, current_app, g
from flask_login import current_user, login_required
from werkzeug.urls import url_parse
from datetime import datetime
from app import db
from app.main import bp
from app.main.forms import EditPlayerForm
from app.models import Player, Game, Match, Team


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    page = request.args.get('page', 1, type=int)
    schedule = Match.query.paginate(
        page, current_app.config['MATCH_PER_PAGE'], False)
    next_url = url_for('main.index', page=schedule.next_num) \
        if schedule.has_next else None
    prev_url = url_for('main.index', page=schedule.prev_num) \
        if schedule.has_prev else None
    return render_template('index.html', title=None, 
        schedule=schedule.items, next_url=next_url, prev_url=prev_url)

@bp.route('/player_edit',  methods=['GET', 'POST'], defaults={'nickname': None})
@bp.route('/player_edit/<nickname>',  methods=['GET', 'POST'])
def player_edit(nickname):
    player = Player.query.filter_by(nickname=nickname).first()
    form = EditPlayerForm(obj=player)
    all_players = Player.query.all()
    if form.validate_on_submit():
        newplayer = Player(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            nickname=form.nickname.data)
        db.session.add(newplayer)
        db.session.commit()
        flash('Player {} {} added!'.format(
            newplayer.first_name, newplayer.last_name))
        return redirect(url_for('main.player_edit'))
    return render_template('edit_player.html', title='Add player', 
        form=form, all_players=all_players)

@bp.route('/match')
@login_required
def match():
    return 0

@bp.route('/team')
@login_required
def team():
    return 0

@bp.route('/search')
@login_required
def search():
    return 0