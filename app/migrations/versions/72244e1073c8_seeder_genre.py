"""seeder_genre

Revision ID: 72244e1073c8
Revises: 143890f5c83d
Create Date: 2025-03-04 23:58:46.891206

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy.orm import Session

from seeders.seeder_genre import seed_master_data

# revision identifiers, used by Alembic.
revision: str = '72244e1073c8'
down_revision: Union[str, None] = '143890f5c83d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    bind = op.get_bind()
    session = Session(bind=bind)

    seed_master_data(session)
    pass


def downgrade() -> None:
    pass
