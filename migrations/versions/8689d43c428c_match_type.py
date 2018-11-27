"""match type

Revision ID: 8689d43c428c
Revises: 201028c9962b
Create Date: 2018-11-27 13:46:17.252024

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8689d43c428c'
down_revision = '201028c9962b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('match', schema=None) as batch_op:
        batch_op.add_column(sa.Column('match_type', sa.String(length=32), nullable=True))
        batch_op.create_index(batch_op.f('ix_match_match_type'), ['match_type'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('match', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_match_match_type'))
        batch_op.drop_column('match_type')

    # ### end Alembic commands ###
