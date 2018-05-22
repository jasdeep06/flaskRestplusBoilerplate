
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager


from app import create_app,db

from app.models import Job,Worker,worker_timesheet,\
    worker_vacantslots,worker_extendedsheet,worker_leavesheet,worker_traveltimesheet

app=create_app('dev')

app.app_context().push()

manager=Manager(app)

migrate=Migrate(app,db)

manager.add_command('db',MigrateCommand)


@manager.command
def run():
    app.run()


if __name__=="__main__":
    manager.run()
