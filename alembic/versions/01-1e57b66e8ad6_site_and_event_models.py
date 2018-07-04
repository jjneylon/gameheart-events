"""Site and Event models

Revision ID: 1e57b66e8ad6
Revises: 
Create Date: 2018-07-03 22:02:49.137808

"""
from alembic import op
import sqlalchemy as db
from sqlalchemy_utils import UUIDType


# revision identifiers, used by Alembic.
revision = '1e57b66e8ad6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'site',
        db.Column('uuid', UUIDType(), primary_key=True),
        db.Column('chapter_uuid', UUIDType()),
        db.Column('title', db.String(32)),
        db.Column('latitude', db.String(32)),
        db.Column('longitude', db.String(32)),
    )

    op.create_table(
        'event',
        db.Column('uuid', UUIDType(), primary_key=True),
        db.Column('site_uuid', UUIDType()),
        db.Column('chapter_uuid', UUIDType()),
        db.Column('title', db.String(32)),
        db.Column('start_time', db.DateTime(timezone=True)),
        db.Column('end_time', db.DateTime(timezone=True)),
    )

    op.create_primary_key('pk_site', 'site', ['uuid'])

    op.create_primary_key('pk_event', 'event', ['uuid'])

    op.create_foreign_key(
        'fk_event_site',
        'event',
        'site',
        ['site_uuid'],
        ['uuid'],
    )


def downgrade():
    op.drop_foreign_key('fk_event_site')

    op.drop_table('event')

    op.drop_table('site')
