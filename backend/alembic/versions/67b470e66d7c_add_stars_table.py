"""Add stars table

Revision ID: 67b470e66d7c
Revises:
Create Date: 2025-01-07 09:52:11.429816

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "67b470e66d7c"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "stars",
        "x_position",
        existing_type=sa.DOUBLE_PRECISION(precision=53),
        nullable=False,
    )
    op.alter_column(
        "stars",
        "y_position",
        existing_type=sa.DOUBLE_PRECISION(precision=53),
        nullable=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "stars",
        "y_position",
        existing_type=sa.DOUBLE_PRECISION(precision=53),
        nullable=True,
    )
    op.alter_column(
        "stars",
        "x_position",
        existing_type=sa.DOUBLE_PRECISION(precision=53),
        nullable=True,
    )
    # ### end Alembic commands ###
