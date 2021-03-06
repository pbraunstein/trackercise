"""users.id is foreign key in rep_exercises_history

Revision ID: 1eb512e3a41e
Revises: 1c15c41f861d
Create Date: 2016-12-31 13:14:18.844672

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1eb512e3a41e'
down_revision = '1c15c41f861d'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column('rep_exercises_history', 'user_id')
    op.add_column('rep_exercises_history', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'rep_exercises_history', 'users', ['user_id'], ['id'])


def downgrade():
    op.drop_constraint('rep_exercises_history_user_id_fkey', 'rep_exercises_history', type_='foreignkey')
    op.drop_column('rep_exercises_history', 'user_id')
    op.add_column('rep_exercises_history', sa.Column('user_id', sa.String()))
