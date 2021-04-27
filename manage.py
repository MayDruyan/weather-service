import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from weather_app import weather_app
from models import db

weather_app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(weather_app, db)
manager = Manager(weather_app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
