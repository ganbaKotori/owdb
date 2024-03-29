"""updated match user hero pks again

Revision ID: bee8e7cc7f20
Revises: 6705403d9eef
Create Date: 2022-09-02 04:20:37.418546

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'bee8e7cc7f20'
down_revision = '6705403d9eef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ow_match', 'user_id')
    op.alter_column('ow_match_user_hero', 'match_user_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.drop_column('ow_match_user_hero', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ow_match_user_hero', sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.alter_column('ow_match_user_hero', 'match_user_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.add_column('ow_match', sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
