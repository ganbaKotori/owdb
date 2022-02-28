"""Adding relation between User and Ranked Matches

Revision ID: d6057a978277
Revises: d97438b7c476
Create Date: 2022-02-27 17:28:32.800830

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6057a978277'
down_revision = 'd97438b7c476'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ranked_match', sa.Column('map_played_id', sa.Integer(), nullable=True))
    op.add_column('ranked_match', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'ranked_match', 'user', ['user_id'], ['id'])
    op.create_foreign_key(None, 'ranked_match', 'ow_map', ['map_played_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'ranked_match', type_='foreignkey')
    op.drop_constraint(None, 'ranked_match', type_='foreignkey')
    op.drop_column('ranked_match', 'user_id')
    op.drop_column('ranked_match', 'map_played_id')
    # ### end Alembic commands ###
