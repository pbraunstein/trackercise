"""Add Users table

Revision ID: 1c15c41f861d
Revises: 80b8617b2cfb
Create Date: 2016-12-31 13:07:20.549874

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '1c15c41f861d'
down_revision = '80b8617b2cfb'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('nickname', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('users')
