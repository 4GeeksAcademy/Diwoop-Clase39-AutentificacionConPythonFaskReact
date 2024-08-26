"""empty message

Revision ID: 7f4fea1556be
Revises: de2ef148e3cf
Create Date: 2024-08-24 14:14:56.451168

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f4fea1556be'
down_revision = 'de2ef148e3cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorite_recepies')
    op.drop_table('favorite_users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorite_users',
    sa.Column('follower_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('followed_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], name='favorite_users_followed_id_fkey'),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], name='favorite_users_follower_id_fkey'),
    sa.PrimaryKeyConstraint('follower_id', 'followed_id', name='favorite_users_pkey')
    )
    op.create_table('favorite_recepies',
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('recepy_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['recepy_id'], ['recepies.id'], name='favorite_recepies_recepy_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='favorite_recepies_user_id_fkey'),
    sa.PrimaryKeyConstraint('user_id', 'recepy_id', name='favorite_recepies_pkey')
    )
    # ### end Alembic commands ###