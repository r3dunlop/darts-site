"""initial

Revision ID: f52d3f860af0
Revises: 
Create Date: 2018-11-19 12:26:11.508561

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f52d3f860af0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('match',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('opponent', sa.String(length=64), nullable=True),
    sa.Column('home_game', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('match', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_match_date'), ['date'], unique=False)
        batch_op.create_index(batch_op.f('ix_match_home_game'), ['home_game'], unique=False)
        batch_op.create_index(batch_op.f('ix_match_opponent'), ['opponent'], unique=False)

    op.create_table('player',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('about_me', sa.String(length=140), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('player', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_player_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_player_name'), ['name'], unique=True)

    op.create_table('game',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('match_id', sa.Integer(), nullable=True),
    sa.Column('game_num', sa.Integer(), nullable=True),
    sa.Column('game_type', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['match_id'], ['match.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('game', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_game_game_num'), ['game_num'], unique=False)
        batch_op.create_index(batch_op.f('ix_game_game_type'), ['game_type'], unique=False)

    op.create_table('player_game',
    sa.Column('player_id', sa.Integer(), nullable=True),
    sa.Column('game_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['game_id'], ['game.id'], ),
    sa.ForeignKeyConstraint(['player_id'], ['player.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('player_game')
    with op.batch_alter_table('game', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_game_game_type'))
        batch_op.drop_index(batch_op.f('ix_game_game_num'))

    op.drop_table('game')
    with op.batch_alter_table('player', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_player_name'))
        batch_op.drop_index(batch_op.f('ix_player_email'))

    op.drop_table('player')
    with op.batch_alter_table('match', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_match_opponent'))
        batch_op.drop_index(batch_op.f('ix_match_home_game'))
        batch_op.drop_index(batch_op.f('ix_match_date'))

    op.drop_table('match')
    # ### end Alembic commands ###
