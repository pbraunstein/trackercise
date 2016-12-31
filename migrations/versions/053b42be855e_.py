"""Create rep_exercises_history table

Revision ID: 053b42be855e
Revises: 
Create Date: 2016-12-15 23:38:49.495889

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '053b42be855e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('rep_exercises_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('sets', sa.Integer(), nullable=True),
    sa.Column('reps', sa.Integer(), nullable=True),
    sa.Column('weight', sa.Float(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('rep_exercises_history')
