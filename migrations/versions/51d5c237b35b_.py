"""empty message

Revision ID: 51d5c237b35b
Revises: d3e5760a943a
Create Date: 2022-01-21 13:36:12.372781

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51d5c237b35b'
down_revision = 'd3e5760a943a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'user', 'queue_number', ['id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    # ### end Alembic commands ###
