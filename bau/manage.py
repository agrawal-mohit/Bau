from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from flask import Flask
from flask_mongoengine import MongoEngine

from app.mod_bau.models import Engineer

import os, sys
import config
from config import BASE_DIR
from app import app, db
import json
import pdb


if BASE_DIR not in sys.path:
	sys.path.append(BASE_DIR)



migrate = Migrate(app, db)
manager = Manager(app)



@manager.command
def init():
	with open(os.path.join(BASE_DIR, 'app/data/engineers.json')) as data_file:
		data = json.load(data_file)
		for eng_data in data:
			try:
				eng = Engineer(**eng_data)
				eng.save()
			except Exception as e:
				print(e)
			else:
				print("Engineers' records added to database")


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

    