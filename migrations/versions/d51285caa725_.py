"""empty message

Revision ID: d51285caa725
Revises: 79a4ff0653c7
Create Date: 2023-07-06 13:29:23.295300

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd51285caa725'
down_revision = '79a4ff0653c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('winers', schema=None) as batch_op:
        batch_op.alter_column('roll',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('winers', schema=None) as batch_op:
        batch_op.alter_column('roll',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###
