"""added accepted column to friendship table

Revision ID: 90d43b5584bf
Revises: 9ec6bb5def62
Create Date: 2022-05-03 14:59:50.669013

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '90d43b5584bf'
down_revision = '9ec6bb5def62'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('friend')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('friend',
    sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('friend_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['friend_id'], ['user.id'], name='friend_ibfk_2'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='friend_ibfk_1'),
    sa.PrimaryKeyConstraint('user_id', 'friend_id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
