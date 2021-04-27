"""empty message

Revision ID: 955b309e09e8
Revises: 
Create Date: 2021-04-24 14:24:09.250209

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '955b309e09e8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('data_point',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('forecast_time', sa.DateTime(), nullable=True),
    sa.Column('temperature', sa.Float(), nullable=True),
    sa.Column('precipitation', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('data_point')
    # ### end Alembic commands ###
