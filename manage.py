import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import app, db

app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def run_importers():
    """
    Not yet implemented
    """
    print 'Hello World!'

if __name__ == '__main__':
    manager.run()