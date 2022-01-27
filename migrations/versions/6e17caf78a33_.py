"""empty message

Revision ID: 6e17caf78a33
Revises: 845ee7730152
Create Date: 2022-01-21 13:50:01.928803

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6e17caf78a33'
down_revision = '845ee7730152'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('slider', 'slider_top_pic',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
    op.alter_column('slider', 'slider_top_line',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
    op.alter_column('slider', 'slider_title',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
    op.alter_column('slider', 'slider_text',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('slider', 'slider_text',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
    op.alter_column('slider', 'slider_title',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
    op.alter_column('slider', 'slider_top_line',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
    op.alter_column('slider', 'slider_top_pic',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
    # ### end Alembic commands ###