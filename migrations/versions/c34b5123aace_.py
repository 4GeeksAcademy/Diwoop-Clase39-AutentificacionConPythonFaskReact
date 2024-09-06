"""empty message

Revision ID: c34b5123aace
Revises: 616ad979d6ad
Create Date: 2024-09-06 09:55:13.859153

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text


# revision identifiers, used by Alembic.
revision = 'c34b5123aace'
down_revision = '616ad979d6ad'
branch_labels = None
depends_on = None


def constraint_exists(constraint_name, table_name):
    conn = op.get_bind()
    result = conn.execute(text(f"""
        SELECT constraint_name
        FROM information_schema.table_constraints
        WHERE table_name = :table_name
        AND constraint_name = :constraint_name
    """), {"table_name": table_name, "constraint_name": constraint_name})
    
    return result.fetchone() is not None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recipe',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('steps', sa.String(length=255), nullable=False),
    sa.Column('is_official', sa.Boolean(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    
    op.execute('DROP TABLE IF EXISTS receta_publicada CASCADE')
    op.drop_table('recetas_publicadas_categorias')
    op.drop_table('recetas_publicadas_ingredients')
    op.execute('DROP TABLE IF EXISTS recepies CASCADE')

    # Modificar la tabla 'categoria_recepies'
    with op.batch_alter_table('categoria_recepies', schema=None) as batch_op:
        if constraint_exists('categoria_recepies_recepy_id_fkey', 'categoria_recepies'):
            batch_op.drop_constraint('categoria_recepies_recepy_id_fkey', type_='foreignkey')

        if constraint_exists('categoria_recepies_receta_publicada_id_fkey', 'categoria_recepies'):
            batch_op.drop_constraint('categoria_recepies_receta_publicada_id_fkey', type_='foreignkey')

        batch_op.create_foreign_key(None, 'recipe', ['recepy_id'], ['id'])
        batch_op.drop_column('receta_publicada_id')

    # Modificar la tabla 'favorite_recepies'
    with op.batch_alter_table('favorite_recepies', schema=None) as batch_op:
        if constraint_exists('favorite_recepies_recepy_id_fkey', 'favorite_recepies'):
            batch_op.drop_constraint('favorite_recepies_recepy_id_fkey', type_='foreignkey')
        
        batch_op.create_foreign_key(None, 'recipe', ['recepy_id'], ['id'])

    # Modificar la tabla 'recepies_ingredients'
    with op.batch_alter_table('recepies_ingredients', schema=None) as batch_op:
        if constraint_exists('recepies_ingredients_recepy_id_fkey', 'recepies_ingredients'):
            batch_op.drop_constraint('recepies_ingredients_recepy_id_fkey', type_='foreignkey')

        batch_op.create_foreign_key(None, 'recipe', ['recepy_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recepies_ingredients', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('recepies_ingredients_recepy_id_fkey', 'recepies', ['recepy_id'], ['id'])

    with op.batch_alter_table('favorite_recepies', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('favorite_recepies_recepy_id_fkey', 'recepies', ['recepy_id'], ['id'])

    with op.batch_alter_table('categoria_recepies', schema=None) as batch_op:
        batch_op.add_column(sa.Column('receta_publicada_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('categoria_recepies_receta_publicada_id_fkey', 'receta_publicada', ['receta_publicada_id'], ['id'])
        batch_op.create_foreign_key('categoria_recepies_recepy_id_fkey', 'recepies', ['recepy_id'], ['id'])

    op.create_table('recepies',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=250), autoincrement=False, nullable=False),
    sa.Column('is_official', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('steps', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='recepies_pkey')
    )
    
    op.create_table('recetas_publicadas_ingredients',
    sa.Column('receta_publicada_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('ingredient_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['ingredient_id'], ['ingredients.id'], name='recetas_publicadas_ingredients_ingredient_id_fkey'),
    sa.ForeignKeyConstraint(['receta_publicada_id'], ['receta_publicada.id'], name='recetas_publicadas_ingredients_receta_publicada_id_fkey'),
    sa.PrimaryKeyConstraint('receta_publicada_id', 'ingredient_id', name='recetas_publicadas_ingredients_pkey')
    )
    
    op.create_table('recetas_publicadas_categorias',
    sa.Column('receta_publicada_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('categoria_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['categoria_id'], ['category.id'], name='recetas_publicadas_categorias_categoria_id_fkey'),
    sa.ForeignKeyConstraint(['receta_publicada_id'], ['receta_publicada.id'], name='recetas_publicadas_categorias_receta_publicada_id_fkey'),
    sa.PrimaryKeyConstraint('receta_publicada_id', 'categoria_id', name='recetas_publicadas_categorias_pkey')
    )
    
    op.create_table('receta_publicada',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=250), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('steps', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('is_official', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='receta_publicada_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='receta_publicada_pkey')
    )
    
    op.drop_table('recipe')
    # ### end Alembic commands ###


