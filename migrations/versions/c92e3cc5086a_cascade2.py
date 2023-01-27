"""cascade2

Revision ID: c92e3cc5086a
Revises: fcd13a85b58e
Create Date: 2023-01-17 13:24:46.590873

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'c92e3cc5086a'
down_revision = 'fcd13a85b58e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('Dish_submenu_id_fkey', 'Dish', type_='foreignkey')
    op.create_foreign_key(None, 'Dish', 'Submenu', ['submenu_id'], ['id'])
    op.drop_constraint('Submenu_menu_id_fkey', 'Submenu', type_='foreignkey')
    op.create_foreign_key(None, 'Submenu', 'Menu', ['menu_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Submenu', type_='foreignkey')
    op.create_foreign_key(
        'Submenu_menu_id_fkey', 'Submenu', 'Menu', [
            'menu_id',
        ], ['id'], ondelete='CASCADE',
    )
    op.drop_constraint(None, 'Dish', type_='foreignkey')
    op.create_foreign_key(
        'Dish_submenu_id_fkey', 'Dish', 'Submenu', [
            'submenu_id',
        ], ['id'], ondelete='CASCADE',
    )
    # ### end Alembic commands ###
