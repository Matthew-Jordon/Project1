"""empty message

Revision ID: 32f5aed2a7f4
Revises: 051e386f2acd
Create Date: 2022-03-20 00:36:18.664168

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32f5aed2a7f4'
down_revision = '051e386f2acd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('property', sa.Column('type', sa.String(length=10), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('property', 'type')
    # ### end Alembic commands ###