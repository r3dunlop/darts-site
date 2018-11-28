"""empty message

Revision ID: 2c52e2402092
Revises: 588aee487285
Create Date: 2018-11-28 15:43:01.442404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c52e2402092'
down_revision = '588aee487285'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('player_season_stats',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('player_id', sa.Integer(), nullable=True),
    sa.Column('season_id', sa.Integer(), nullable=True),
    sa.Column('matches_played', sa.Integer(), nullable=False),
    sa.Column('matches_won', sa.Integer(), nullable=False),
    sa.Column('matches_lost', sa.Integer(), nullable=False),
    sa.Column('games_played', sa.Integer(), nullable=False),
    sa.Column('games_won', sa.Integer(), nullable=False),
    sa.Column('games_lost', sa.Integer(), nullable=False),
    sa.Column('total_stars', sa.Integer(), nullable=False),
    sa.Column('total_high_scores', sa.Integer(), nullable=False),
    sa.Column('total_low_scores', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['player_id'], ['player.id'], name=op.f('fk_player_season_stats_player_id_player')),
    sa.ForeignKeyConstraint(['season_id'], ['season.id'], name=op.f('fk_player_season_stats_season_id_season')),
    sa.PrimaryKeyConstraint('id', 'matches_played', 'matches_won', 'matches_lost', 'games_played', 'games_won', 'games_lost', 'total_stars', 'total_high_scores', 'total_low_scores', name=op.f('pk_player_season_stats'))
    )
    op.create_table('team_season_stats',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('season_id', sa.Integer(), nullable=True),
    sa.Column('matches_played', sa.Integer(), nullable=False),
    sa.Column('matches_won', sa.Integer(), nullable=False),
    sa.Column('matches_lost', sa.Integer(), nullable=False),
    sa.Column('games_played', sa.Integer(), nullable=False),
    sa.Column('games_won', sa.Integer(), nullable=False),
    sa.Column('total_stars', sa.Integer(), nullable=False),
    sa.Column('total_high_scores', sa.Integer(), nullable=False),
    sa.Column('total_low_scores', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['season_id'], ['season.id'], name=op.f('fk_team_season_stats_season_id_season')),
    sa.PrimaryKeyConstraint('id', 'matches_played', 'matches_won', 'matches_lost', 'games_played', 'games_won', 'total_stars', 'total_high_scores', 'total_low_scores', name=op.f('pk_team_season_stats'))
    )
    op.drop_table('player_season_statistics')
    op.drop_table('team_season_statistics')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('team_season_statistics',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('season_id', sa.INTEGER(), nullable=True),
    sa.Column('matches_played', sa.INTEGER(), nullable=False),
    sa.Column('matches_won', sa.INTEGER(), nullable=False),
    sa.Column('matches_lost', sa.INTEGER(), nullable=False),
    sa.Column('games_played', sa.INTEGER(), nullable=False),
    sa.Column('games_won', sa.INTEGER(), nullable=False),
    sa.Column('total_stars', sa.INTEGER(), nullable=False),
    sa.Column('total_high_scores', sa.INTEGER(), nullable=False),
    sa.Column('total_low_scores', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['season_id'], ['season.id'], name='fk_team_season_statistics_season_id_season'),
    sa.PrimaryKeyConstraint('id', 'matches_played', 'matches_won', 'matches_lost', 'games_played', 'games_won', 'total_stars', 'total_high_scores', 'total_low_scores', name='pk_team_season_statistics')
    )
    op.create_table('player_season_statistics',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('matches_played', sa.INTEGER(), nullable=False),
    sa.Column('matches_won', sa.INTEGER(), nullable=False),
    sa.Column('matches_lost', sa.INTEGER(), nullable=False),
    sa.Column('games_played', sa.INTEGER(), nullable=False),
    sa.Column('games_won', sa.INTEGER(), nullable=False),
    sa.Column('total_stars', sa.INTEGER(), nullable=False),
    sa.Column('total_high_scores', sa.INTEGER(), nullable=False),
    sa.Column('total_low_scores', sa.INTEGER(), nullable=False),
    sa.Column('season_id', sa.INTEGER(), nullable=True),
    sa.Column('player_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['player_id'], ['player.id'], name='fk_player_season_statistics_player_id_player'),
    sa.ForeignKeyConstraint(['season_id'], ['season.id'], name='fk_player_season_statistics_season_id_season'),
    sa.PrimaryKeyConstraint('id', 'matches_played', 'matches_won', 'matches_lost', 'games_played', 'games_won', 'total_stars', 'total_high_scores', 'total_low_scores', name='pk_player_season_statistics')
    )
    op.drop_table('team_season_stats')
    op.drop_table('player_season_stats')
    # ### end Alembic commands ###
