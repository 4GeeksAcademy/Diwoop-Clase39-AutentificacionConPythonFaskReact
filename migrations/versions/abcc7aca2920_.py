"""empty message

Revision ID: abcc7aca2920
Revises: aa3aaa052038
Create Date: 2024-08-21 10:29:49.960594

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'abcc7aca2920'
down_revision = 'aa3aaa052038'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ingredients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('recepies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('categoria_recepies',
    sa.Column('recepy_id', sa.Integer(), nullable=False),
    sa.Column('categoria_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['categoria_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['recepy_id'], ['recepies.id'], ),
    sa.PrimaryKeyConstraint('recepy_id', 'categoria_id')
    )
    op.create_table('favorite_recepies',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('recepy_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['recepy_id'], ['recepies.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'recepy_id')
    )
    op.create_table('recepies_ingredients',
    sa.Column('recepy_id', sa.Integer(), nullable=False),
    sa.Column('ingredient_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['ingredient_id'], ['ingredients.id'], ),
    sa.ForeignKeyConstraint(['recepy_id'], ['recepies.id'], ),
    sa.PrimaryKeyConstraint('recepy_id', 'ingredient_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recepies_ingredients')
    op.drop_table('favorite_recepies')
    op.drop_table('categoria_recepies')
    op.drop_table('recepies')
    op.drop_table('ingredients')
    op.drop_table('category')
    # ### end Alembic commands ###
