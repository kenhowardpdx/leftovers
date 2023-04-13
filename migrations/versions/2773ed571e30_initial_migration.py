"""Initial Migration

Revision ID: 2773ed571e30
Revises: 
Create Date: 2023-04-13 08:48:04.897112

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2773ed571e30'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.execute("INSERT INTO users (username, email) VALUES ('default', 'none@none')")


def downgrade():
    op.drop_table('users')
