"""update to pk and fk for MatchUser and MatchUserHero

Revision ID: d975d87331c2
Revises: d233347ec020
Create Date: 2022-07-28 17:10:58.552069

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd975d87331c2'
down_revision = 'd233347ec020'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ow_match_user_hero', sa.Column('id', sa.Integer(), autoincrement=True, nullable=False))
    op.add_column('ow_match_user_hero', sa.Column('match_user_id', sa.Integer(), nullable=False))
    op.drop_constraint('ow_match_user_hero_ibfk_1', 'ow_match_user_hero', type_='foreignkey')
    op.drop_constraint('ow_match_user_hero_ibfk_4', 'ow_match_user_hero', type_='foreignkey')
    op.create_foreign_key(None, 'ow_match_user_hero', 'ow_match_user', ['match_user_id'], ['id'])
    op.drop_column('ow_match_user_hero', 'match_id')
    op.drop_column('ow_match_user_hero', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ow_match_user_hero', sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.add_column('ow_match_user_hero', sa.Column('match_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'ow_match_user_hero', type_='foreignkey')
    op.create_foreign_key('ow_match_user_hero_ibfk_4', 'ow_match_user_hero', 'ow_match_user', ['user_id'], ['user_id'])
    op.create_foreign_key('ow_match_user_hero_ibfk_1', 'ow_match_user_hero', 'ow_match', ['match_id'], ['id'])
    op.drop_column('ow_match_user_hero', 'match_user_id')
    op.drop_column('ow_match_user_hero', 'id')
    # ### end Alembic commands ###
