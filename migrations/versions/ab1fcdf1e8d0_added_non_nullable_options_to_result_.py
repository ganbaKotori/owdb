"""added non-nullable options to Result and Phase column in Match Round

Revision ID: ab1fcdf1e8d0
Revises: 27b4c24bb230
Create Date: 2022-05-06 16:15:10.386571

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ab1fcdf1e8d0'
down_revision = '27b4c24bb230'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('ow_match_round', 'objectives_captured',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False)
    op.alter_column('ow_match_round', 'phase',
               existing_type=mysql.ENUM('ATTACK', 'DEFEND', 'CONTROL'),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('ow_match_round', 'phase',
               existing_type=mysql.ENUM('ATTACK', 'DEFEND', 'CONTROL'),
               nullable=True)
    op.alter_column('ow_match_round', 'objectives_captured',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True)
    # ### end Alembic commands ###
