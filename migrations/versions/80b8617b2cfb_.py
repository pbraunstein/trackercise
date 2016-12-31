"""Add foreign key of exercise id to rep exercises history table

Revision ID: 80b8617b2cfb
Revises: a0620f5c7597
Create Date: 2016-12-30 21:20:26.867267

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80b8617b2cfb'
down_revision = 'a0620f5c7597'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rep_exercises_history', sa.Column('exercise_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'rep_exercises_history', 'rep_exercises_taxonomy', ['exercise_id'], ['id'])
    op.drop_column('rep_exercises_history', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rep_exercises_history', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'rep_exercises_history', type_='foreignkey')
    op.drop_column('rep_exercises_history', 'exercise_id')
    # ### end Alembic commands ###
