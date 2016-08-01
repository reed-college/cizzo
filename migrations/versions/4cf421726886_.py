"""empty message

Revision ID: 4cf421726886
Revises: None
Create Date: 2016-08-01 14:39:12.047731

"""

# revision identifiers, used by Alembic.
revision = '4cf421726886'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('locations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('building', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('locgroups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('typecategories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('groupmapping',
    sa.Column('loc_id', sa.Integer(), nullable=True),
    sa.Column('locgroup_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['loc_id'], ['locations.id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['locgroup_id'], ['locgroups.id'], ondelete='cascade')
    )
    op.create_table('incidents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('datetime', sa.DateTime(), nullable=True),
    sa.Column('summary', sa.String(length=500), nullable=True),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['locations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=15), nullable=True),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.Column('typecategory', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['typecategory'], ['typecategories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mapping',
    sa.Column('type_id', sa.Integer(), nullable=True),
    sa.Column('incident_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['incident_id'], ['incidents.id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['type_id'], ['types.id'], ondelete='cascade')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mapping')
    op.drop_table('types')
    op.drop_table('incidents')
    op.drop_table('groupmapping')
    op.drop_table('typecategories')
    op.drop_table('locgroups')
    op.drop_table('locations')
    ### end Alembic commands ###