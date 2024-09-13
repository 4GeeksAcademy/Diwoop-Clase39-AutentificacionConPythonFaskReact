"""empty message

Revision ID: f4abfc67ff14
Revises: ab2f9e433201
Create Date: 2024-09-13 00:29:23.856188

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4abfc67ff14'
down_revision = 'ab2f9e433201'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('bio', sa.String(length=500), nullable=True))
        batch_op.add_column(sa.Column('profile_image', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('profile_image')
        batch_op.drop_column('bio')

    # ### end Alembic commands ###
