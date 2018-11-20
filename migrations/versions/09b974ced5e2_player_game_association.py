"""player_game association
Revision ID: 09b974ced5e2
Revises: 6425cdc4c19a
Create Date: 2018-11-19 14:04:57.984778
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09b974ced5e2'
down_revision = '6425cdc4c19a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('player_game', schema=None) as batch_op:
        batch_op.add_column(sa.Column('stars', sa.Integer(), nullable=True))
        batch_op.create_index(batch_op.f('ix_player_game_stars'), ['stars'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('player_game', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_player_game_stars'))
        batch_op.drop_column('stars')

    # ### end Alembic commands ###