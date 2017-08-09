"""Adds TimeExercisesHistory and TimeExercisesTaxonomy Tables

Revision ID: 7791f2c862d2
Revises: 56630a78dca0
Create Date: 2017-07-30 20:40:17.174425

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '7791f2c862d2'
down_revision = '56630a78dca0'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'time_exercises_taxonomy',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )
    op.create_table(
        'time_exercises_history',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('exercise_id', sa.Integer(), nullable=True),
        sa.Column('distance', sa.Float(), nullable=True),
        sa.Column('duration', sa.Float(), nullable=True),
        sa.Column('exercise_date', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['exercise_id'], ['time_exercises_history.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('time_exercises_history')
    op.drop_table('time_exercises_taxonomy')
