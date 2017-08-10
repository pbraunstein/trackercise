"""Foreign key for time exercises history should be from time exercises taxonomy not itself

Revision ID: 5ea00754f4a1
Revises: a12842d65064
Create Date: 2017-08-08 09:17:12.088281

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '5ea00754f4a1'
down_revision = 'a12842d65064'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_constraint(u'time_exercises_history_exercise_id_fkey', 'time_exercises_history', type_='foreignkey')
    op.create_foreign_key(u'time_exercises_history_exercise_id_fkey', 'time_exercises_history',
                          'time_exercises_taxonomy', ['exercise_id'], ['id'])


def downgrade():
    op.drop_constraint(u'time_exercises_history_exercise_id_fkey', 'time_exercises_history', type_='foreignkey')
    op.create_foreign_key(u'time_exercises_history_exercise_id_fkey', 'time_exercises_history',
                          'time_exercises_history', ['exercise_id'], ['id'])
