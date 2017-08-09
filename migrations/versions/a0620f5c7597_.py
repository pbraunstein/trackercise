"""Add rep exercises taxonomy table

Revision ID: a0620f5c7597
Revises: 053b42be855e
Create Date: 2016-12-28 11:03:42.904961

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'a0620f5c7597'
down_revision = '053b42be855e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'rep_exercises_taxonomy',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('is_back', sa.Boolean(), nullable=True),
        sa.Column('is_chest', sa.Boolean(), nullable=True),
        sa.Column('is_shoulders', sa.Boolean(), nullable=True),
        sa.Column('is_biceps', sa.Boolean(), nullable=True),
        sa.Column('is_triceps', sa.Boolean(), nullable=True),
        sa.Column('is_legs', sa.Boolean(), nullable=True),
        sa.Column('is_core', sa.Boolean(), nullable=True),
        sa.Column('is_balance', sa.Boolean(), nullable=True),
        sa.Column('is_cardio', sa.Boolean(), nullable=True),
        sa.Column('is_weight_per_hand', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('rep_exercises_taxonomy')
