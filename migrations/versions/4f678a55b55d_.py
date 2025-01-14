"""empty message

Revision ID: 4f678a55b55d
Revises: dd7a8a9196fe
Create Date: 2024-08-14 11:53:00.833749

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f678a55b55d'
down_revision = 'dd7a8a9196fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.add_column(sa.Column('gender', sa.String(length=250), nullable=True))
        batch_op.add_column(sa.Column('hair_color', sa.String(length=250), nullable=True))
        batch_op.add_column(sa.Column('skin_color', sa.String(length=250), nullable=True))

    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.add_column(sa.Column('orbital_period', sa.String(length=250), nullable=True))
        batch_op.add_column(sa.Column('rotation_period', sa.String(length=250), nullable=True))
        batch_op.add_column(sa.Column('terrain', sa.String(length=250), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.drop_column('terrain')
        batch_op.drop_column('rotation_period')
        batch_op.drop_column('orbital_period')

    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.drop_column('skin_color')
        batch_op.drop_column('hair_color')
        batch_op.drop_column('gender')

    # ### end Alembic commands ###
