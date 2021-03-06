"""removed objectives_cleared column from match round

Revision ID: adbc801d8b1b
Revises: 9b05206b1f6f
Create Date: 2022-05-17 01:51:39.973172

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'adbc801d8b1b'
down_revision = '9b05206b1f6f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ow_match_round', 'objectives_captured')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ow_match_round', sa.Column('objectives_captured', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
