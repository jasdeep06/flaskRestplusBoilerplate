"""empty message

Revision ID: 6dfc53b4e2f0
Revises: 
Create Date: 2018-05-22 19:27:40.124925

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6dfc53b4e2f0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('job',
    sa.Column('request_ref', sa.String(), autoincrement=False, nullable=False),
    sa.Column('priority', sa.Integer(), nullable=True),
    sa.Column('job_type_desc', sa.String(), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('initial_estimate_hours', sa.Integer(), nullable=True),
    sa.Column('start_after', sa.String(), nullable=True),
    sa.Column('due_ts', sa.String(), nullable=True),
    sa.Column('dependency', sa.String(), nullable=True),
    sa.Column('assigned', sa.Integer(), nullable=True),
    sa.Column('technician', sa.Integer(), nullable=True),
    sa.Column('assigned_start', sa.String(), nullable=True),
    sa.Column('assigned_end', sa.String(), nullable=True),
    sa.Column('skills', sa.String(), nullable=True),
    sa.Column('core_area', sa.String(), nullable=True),
    sa.Column('location_code', sa.String(), nullable=True),
    sa.Column('job_source', sa.String(), nullable=True),
    sa.Column('job_type', sa.String(), nullable=True),
    sa.Column('target_attended_ts', sa.String(), nullable=True),
    sa.Column('target_attended_duration', sa.Integer(), nullable=True),
    sa.Column('job_state', sa.String(), nullable=True),
    sa.Column('attended_ts', sa.String(), nullable=True),
    sa.Column('attend_days_to_due', sa.Integer(), nullable=True),
    sa.Column('attend_hours_to_due', sa.Integer(), nullable=True),
    sa.Column('job_lock', sa.Integer(), nullable=True),
    sa.Column('original_due_ts', sa.String(), nullable=True),
    sa.Column('due_month', sa.Integer(), nullable=True),
    sa.Column('days_to_due', sa.Integer(), nullable=True),
    sa.Column('hours_to_due', sa.Integer(), nullable=True),
    sa.Column('wait_state', sa.Integer(), nullable=True),
    sa.Column('wait_reason', sa.String(), nullable=True),
    sa.Column('job_status', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('request_ref')
    )
    op.create_table('worker',
    sa.Column('user_id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('emailid', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('type', sa.Integer(), nullable=True),
    sa.Column('default_days', sa.String(), nullable=True),
    sa.Column('start_time', sa.String(), nullable=True),
    sa.Column('end_time', sa.String(), nullable=True),
    sa.Column('jobs_assigned', sa.String(), nullable=True),
    sa.Column('skills', sa.String(), nullable=True),
    sa.Column('default_latitude', sa.Float(), nullable=True),
    sa.Column('default_longitude', sa.Float(), nullable=True),
    sa.Column('blacklisted_latlongs', sa.String(), nullable=True),
    sa.Column('phone_number', sa.Integer(), nullable=True),
    sa.Column('firstname', sa.String(), nullable=True),
    sa.Column('lastname', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('active_ind', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('emailid')
    )
    op.create_table('worker_extendedsheet',
    sa.Column('user_id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('extendedsheet', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('worker_leavesheet',
    sa.Column('user_id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('leavesheet', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('worker_timesheet',
    sa.Column('user_id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('timesheet', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('worker_traveltimesheet',
    sa.Column('user_id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('travel_timesheet', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('worker_vacantslots',
    sa.Column('user_id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('vacantslots', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('worker_vacantslots')
    op.drop_table('worker_traveltimesheet')
    op.drop_table('worker_timesheet')
    op.drop_table('worker_leavesheet')
    op.drop_table('worker_extendedsheet')
    op.drop_table('worker')
    op.drop_table('job')
    # ### end Alembic commands ###
