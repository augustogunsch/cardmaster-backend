"""Increase password field length

Revision ID: 108906988dc3
Revises: a5ff58b95fec
Create Date: 2023-11-08 14:17:44.026819

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '108906988dc3'
down_revision = 'a5ff58b95fec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.String(length=162),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.String(length=162),
               type_=sa.VARCHAR(length=128),
               existing_nullable=False)

    # ### end Alembic commands ###
