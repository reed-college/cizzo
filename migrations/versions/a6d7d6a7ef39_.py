"""empty message

Revision ID: a6d7d6a7ef39
Revises: 2e8330808ca4
Create Date: 2016-06-09 10:02:04.612412

"""

# revision identifiers, used by Alembic.
revision = 'a6d7d6a7ef39'
down_revision = '2e8330808ca4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('incidents', sa.Column('eventtype', sa.String(length=25), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('incidents', 'eventtype')
    ### end Alembic commands ###