from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from flask import Flask
from flask_mongoengine import MongoEngine

import os, sys
import config
from config import BASE_DIR
from app import app, db

sys.path.append(BASE_DIR)




#BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))




migrate = Migrate(app, db)
manager = Manager(app)


manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(
		use_debugger = True,
		use_reloader=True,
		host='0.0.0.0',
		port=9090
	))
if __name__ == '__main__':
    manager.run()
    print("Server running at localhost:9000")

    