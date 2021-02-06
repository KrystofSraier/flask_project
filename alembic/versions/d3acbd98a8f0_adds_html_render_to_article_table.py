"""adds html render to article table

Revision ID: d3acbd98a8f0
Revises: 362c7d65017b
Create Date: 2021-02-06 09:15:29.254765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3acbd98a8f0'
down_revision = '362c7d65017b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("article",
        sa.Column("html_render", sa.String, server_default=""))


def downgrade():
    op.drop_column("article", "html_render")
