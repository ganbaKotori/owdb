"""added Result and Phase column to Match Round

Revision ID: 27b4c24bb230
Revises: b13758d100d5
Create Date: 2022-05-06 16:13:10.279569

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27b4c24bb230'
down_revision = 'b13758d100d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ow_match_round', sa.Column('objectives_captured', sa.Boolean(), nullable=True))
    op.add_column('ow_match_round', sa.Column('phase', sa.Enum('ATTACK', 'DEFEND', 'CONTROL', name='matchphase'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ow_match_round', 'phase')
    op.drop_column('ow_match_round', 'objectives_captured')
    # ### end Alembic commands ###