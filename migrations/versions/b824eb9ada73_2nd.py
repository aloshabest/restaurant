"""2nd

Revision ID: b824eb9ada73
Revises: cdf621ef92e9
Create Date: 2023-01-16 13:20:41.729938

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b824eb9ada73'
down_revision = 'cdf621ef92e9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Dish',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_index(op.f('ix_Dish_id'), 'Dish', ['id'], unique=True)
    op.create_table('Submenu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('dish', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['dish'], ['Dish.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_index(op.f('ix_Submenu_id'), 'Submenu', ['id'], unique=True)
    op.add_column('Menu', sa.Column('submenu', sa.Integer(), nullable=True))
    op.create_unique_constraint(None, 'Menu', ['title'])
    op.create_foreign_key(None, 'Menu', 'Submenu', ['submenu'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Menu', type_='foreignkey')
    op.drop_constraint(None, 'Menu', type_='unique')
    op.drop_column('Menu', 'submenu')
    op.drop_index(op.f('ix_Submenu_id'), table_name='Submenu')
    op.drop_table('Submenu')
    op.drop_index(op.f('ix_Dish_id'), table_name='Dish')
    op.drop_table('Dish')
    # ### end Alembic commands ###