"""add role to user

Revision ID: e987b3608c74
Revises: 53ec60ee98bb
Create Date: 2019-06-20 14:18:47.135512

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e987b3608c74'
down_revision = '53ec60ee98bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('role', sa.String(length=32), nullable=True))
        batch_op.create_index(batch_op.f('ix_user_role'), ['role'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_role'))
        batch_op.drop_column('role')

    # ### end Alembic commands ###
