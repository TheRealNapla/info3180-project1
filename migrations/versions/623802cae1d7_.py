"""empty message

Revision ID: 623802cae1d7
Revises: 
Create Date: 2023-03-12 12:34:32.647153

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '623802cae1d7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('properties',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('desc', sa.Text(), nullable=True),
    sa.Column('bedsno', sa.Integer(), nullable=True),
    sa.Column('bathsno', sa.Integer(), nullable=True),
    sa.Column('price', sa.String(length=30), nullable=True),
    sa.Column('propertytype', sa.String(length=20), nullable=True),
    sa.Column('location', sa.String(length=200), nullable=True),
    sa.Column('pic', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('properties')
    # ### end Alembic commands ###
