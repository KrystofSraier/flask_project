"""create users table

Revision ID: 362c7d65017b
Revises: 
Create Date: 2021-01-27 06:49:20.170196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '362c7d65017b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
            "user",
            sa.Column("id", sa.Integer, primary_key=True),
            sa.Column("username", sa.String),
            sa.Column("password", sa.String))


def downgrade():
    op.drop_table("user")
