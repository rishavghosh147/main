"""empty message

Revision ID: 18a75a4bc424
Revises: de747cf1d983
Create Date: 2023-07-16 06:14:11.811919

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18a75a4bc424'
down_revision = 'de747cf1d983'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('event', schema=None) as batch_op:
        batch_op.alter_column('about_event',
               existing_type=sa.VARCHAR(length=500),
               type_=sa.String(length=5000),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('event', schema=None) as batch_op:
        batch_op.alter_column('about_event',
               existing_type=sa.String(length=5000),
               type_=sa.VARCHAR(length=500),
               existing_nullable=False)

    # ### end Alembic commands ###
