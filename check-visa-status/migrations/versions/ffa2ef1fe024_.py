"""empty message

Revision ID: ffa2ef1fe024
Revises: fe2338f07f93
Create Date: 2021-09-29 20:33:17.196916

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer

# revision identifiers, used by Alembic.
revision = 'ffa2ef1fe024'
down_revision = 'fe2338f07f93'
branch_labels = None
depends_on = None


def upgrade():
    visa_status = table('visa_status',
    column('id', Integer),
    column('name', String),
    column('visa_num', String),
    column('status',String)
)
    op.bulk_insert(visa_status,
    [
        {'id':1, 'name':'John Smith',
                'visa_num':'123456789',
                'status':'available'},
        {'id':2, 'name':'Ed Williams',
                'visa_num':'234567890'
                ,'status':'available'},
        {'id':3, 'name':'Wendy Jones',
                'visa_num':'345678901',
                'status':'available'},
    ]
)

def downgrade():
    pass
