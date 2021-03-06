"""Make Users table compatible with Flask-Login

Revision ID: ed3110b30b84
Revises: 1eb512e3a41e
Create Date: 2017-01-16 15:28:40.324500

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed3110b30b84'
down_revision = '1eb512e3a41e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('authenticated', sa.Boolean(), nullable=True))
    op.add_column('users', sa.Column('email', sa.String(), nullable=True))
    op.add_column('users', sa.Column('password', sa.String(), nullable=True))


def downgrade():
    op.drop_column('users', 'password')
    op.drop_column('users', 'email')
    op.drop_column('users', 'authenticated')
