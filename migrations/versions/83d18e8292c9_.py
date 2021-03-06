"""empty message

Revision ID: 83d18e8292c9
Revises: 
Create Date: 2021-05-24 16:41:01.710907

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83d18e8292c9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('registered_on', sa.DateTime(), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=False),
    sa.Column('confirmed', sa.Boolean(), nullable=False),
    sa.Column('confirmed_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
