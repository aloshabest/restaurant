"""numeric

Revision ID: 6e36d692768b
Revises: c92e3cc5086a
Create Date: 2023-01-17 13:58:39.304803

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '6e36d692768b'
down_revision = 'c92e3cc5086a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        'Dish', 'price',
        existing_type=postgresql.DOUBLE_PRECISION(precision=53),
        nullable=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        'Dish', 'price',
        existing_type=postgresql.DOUBLE_PRECISION(precision=53),
        nullable=True,
    )
    # ### end Alembic commands ###
