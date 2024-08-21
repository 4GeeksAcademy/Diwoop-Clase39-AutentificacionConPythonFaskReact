"""empty message

Revision ID: 25e1d473aaf2
Revises: 248f6d8c080e
Create Date: 2024-08-21 08:50:50.791389

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25e1d473aaf2'
down_revision = '248f6d8c080e'
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