"""Add Deck model and many-to-many relationship

Revision ID: ea67832a49a5
Revises: da3119b9ecfd
Create Date: 2023-09-13 09:42:51.517485

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea67832a49a5'
down_revision = 'da3119b9ecfd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('deck',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('deck_user_association',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('deck_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['deck_id'], ['deck.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('deck_user_association')
    op.drop_table('deck')
    # ### end Alembic commands ###
