from . import db


class Job(db.Model):
    request_ref = db.Column(db.String, primary_key=True,autoincrement=False)
    priority = db.Column(db.Integer, unique=False)
    job_type_desc = db.Column(db.String, unique=False)
    latitude=db.Column(db.Float,unique=False)
    longitude=db.Column(db.Float,unique=False)
    initial_estimate_hours=db.Column(db.Integer, unique=False)
    start_after=db.Column(db.String, unique=False)
    due_ts=db.Column(db.String, unique=False)
    dependency=db.Column(db.String, unique=False)
    assigned=db.Column(db.Integer,unique=False,default=0)
    technician=db.Column(db.Integer,unique=False)
    assigned_start=db.Column(db.String,unique=False)
    assigned_end = db.Column(db.String, unique=False)
    skills=db.Column(db.String,unique=False)
    core_area = db.Column(db.String, unique=False)
    location_code = db.Column(db.String, unique=False)
    job_source = db.Column(db.String, unique=False)
    job_type=db.Column(db.String, unique=False)
    target_attended_ts=db.Column(db.String, unique=False)
    target_attended_duration=db.Column(db.Integer, unique=False)
    job_state=db.Column(db.String,unique=False)
    attended_ts=db.Column(db.String,unique=False)
    attend_days_to_due=db.Column(db.Integer,unique=False)
    attend_hours_to_due=db.Column(db.Integer,unique=False)
    job_lock=db.Column(db.Integer,unique=False,default=0)
    original_due_ts=db.Column(db.String,unique=False)
    due_month=db.Column(db.Integer,unique=False)
    days_to_due=db.Column(db.Integer,unique=False)
    hours_to_due=db.Column(db.Integer,unique=False)
    wait_state=db.Column(db.Integer,unique=False,default=0)
    wait_reason=db.Column(db.String,unique=False,default="Feeling Sleepy")
    job_status=db.Column(db.String,unique=False,default="New")







    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return "<Job {0.id}: {0.start_after} {0.end_before}>".format(self)










class Worker(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    emailid = db.Column(db.String, unique=True)
    location = db.Column(db.String, unique=False)
    type = db.Column(db.Integer, unique=False)
    default_days = db.Column(db.String, unique=False)
    start_time = db.Column(db.String, unique=False)
    end_time = db.Column(db.String, unique=False)
    jobs_assigned=db.Column(db.String,unique=False)
    skills=db.Column(db.String,unique=False)
    default_latitude=db.Column(db.Float,unique=False)
    default_longitude=db.Column(db.Float,unique=False)
    blacklisted_latlongs=db.Column(db.String,unique=False)
    phone_number = db.Column(db.Integer,unique=False)
    firstname=db.Column(db.String,unique=False)
    lastname=db.Column(db.String,unique=False)
    username=db.Column(db.String,unique=False,default="")

    active_ind=db.Column(db.Integer,unique=False,default=1)






class worker_timesheet(db.Model):
    user_id=db.Column(db.Integer, primary_key=True, autoincrement=False)
    timesheet=db.Column(db.String,unique=False)


class worker_extendedsheet(db.Model):
    user_id=db.Column(db.Integer, primary_key=True, autoincrement=False)
    extendedsheet = db.Column(db.String, unique=False)

class worker_leavesheet(db.Model):
    user_id=db.Column(db.Integer, primary_key=True, autoincrement=False)
    leavesheet = db.Column(db.String, unique=False)

class worker_vacantslots(db.Model):
    user_id=db.Column(db.Integer, primary_key=True, autoincrement=False)
    vacantslots = db.Column(db.String, unique=False)




class worker_traveltimesheet(db.Model):
    user_id=db.Column(db.Integer, primary_key=True, autoincrement=False)
    travel_timesheet=db.Column(db.String,unique=False)
