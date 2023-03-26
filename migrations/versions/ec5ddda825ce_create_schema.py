"""create schema

Revision ID: ec5ddda825ce
Revises:
Create Date: 2023-01-22 15:43:12.663404

"""
from alembic import op
import sqlalchemy as sa

from datetime import datetime as dt

# revision identifiers, used by Alembic.
revision = 'ec5ddda825ce'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'flags',
        sa.Column('flag_id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(64), nullable=False),
        sa.Column('value', sa.String(64), nullable=False),
        sa.Column('status', sa.Boolean, nullable=False),
    )


def downgrade() -> None:
    op.drop_table('flags')
