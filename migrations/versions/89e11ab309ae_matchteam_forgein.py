"""matchteam forgein

Revision ID: 89e11ab309ae
Revises: e3ea144378fc
Create Date: 2018-11-20 18:42:33.897427

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89e11ab309ae'
down_revision = 'e3ea144378fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('match', schema=None) as batch_op:
        batch_op.add_column(sa.Column('opponent_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('opponent_id', 'team', ['opponent_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('match', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('opponent_id')

    # ### end Alembic commands ###
