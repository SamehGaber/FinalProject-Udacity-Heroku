"""empty message

Revision ID: e00440f0c026
Revises: 
Create Date: 2020-04-26 14:14:23.957233

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e00440f0c026'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movie', sa.Column('dummmy', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('movie', 'dummmy')
    # ### end Alembic commands ###
