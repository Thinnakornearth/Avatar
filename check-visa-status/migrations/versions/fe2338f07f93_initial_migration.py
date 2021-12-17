"""initial migration

Revision ID: fe2338f07f93
Revises: 
Create Date: 2021-09-29 20:28:20.472325

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe2338f07f93'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('visa_status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('visa_num', sa.String(length=15), nullable=False),
    sa.Column('status', sa.String(length=15), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('visa_status')
    # ### end Alembic commands ###