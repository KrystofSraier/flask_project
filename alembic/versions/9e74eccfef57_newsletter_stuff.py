"""newsletter stuff

Revision ID: 9e74eccfef57
Revises: d3acbd98a8f0
Create Date: 2021-02-07 09:22:26.901379

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e74eccfef57'
down_revision = 'd3acbd98a8f0'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "newsletter",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("email", sa.String, unique=True))


def downgrade():
    op.drop_trable("newsletter")
