"""User email must be unique and non-nullable

Revision ID: 56630a78dca0
Revises: ed3110b30b84
Create Date: 2017-01-25 08:46:37.652600

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '56630a78dca0'
down_revision = 'ed3110b30b84'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'email',
                    existing_type=sa.VARCHAR(),
                    nullable=False)
    op.create_unique_constraint('users_email_key', 'users', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('users_email_key', 'users', type_='unique')
    op.alter_column('users', 'email',
                    existing_type=sa.VARCHAR(),
                    nullable=True)
    # ### end Alembic commands ###
