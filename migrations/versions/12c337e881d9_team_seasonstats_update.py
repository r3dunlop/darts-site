"""team seasonstats update

Revision ID: 12c337e881d9
Revises: 89a6f42ad800
Create Date: 2018-12-04 20:11:17.405986

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12c337e881d9'
down_revision = '89a6f42ad800'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('team_season_stats', schema=None) as batch_op:
        batch_op.add_column(sa.Column('games_lost', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('team_season_stats', schema=None) as batch_op:
        batch_op.drop_column('games_lost')

    # ### end Alembic commands ###
