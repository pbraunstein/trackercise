"""Time Exercise History duration should be int

Revision ID: a12842d65064
Revises: 7791f2c862d2
Create Date: 2017-08-08 07:50:16.607262

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a12842d65064'
down_revision = '7791f2c862d2'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('time_exercises_history', 'duration',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               type_=sa.Integer(),
               existing_nullable=True)


def downgrade():
    op.alter_column('time_exercises_history', 'duration',
               existing_type=sa.Integer(),
               type_=postgresql.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)
