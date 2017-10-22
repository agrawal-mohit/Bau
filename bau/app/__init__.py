import os

# Import flask and template operators
from flask import Flask, render_template
from flask_mongoengine import MongoEngine
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_wtf import CsrfProtect

# import pytz
# from pytz import utc
from datetime import datetime


import csv
import logging
import datetime
import config

# Define the WSGI application object
app = Flask(__name__ , static_url_path='/static')

app.config.from_object(config.DevelopmentConfig)
db = MongoEngine(app)


bcrypt = Bcrypt(app)
app.debug = True
#CsrfProtect(app)
# Import a module / component using its blueprint handler variable (mod_user)

from app.mod_bau.controllers       import mod_bau          as bau_module


# Register blueprint(s)
app.register_blueprint(bau_module)


"""
jobstores = {
    'mongo': MongoDBJobStore()
}
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}

print(datetime.utcnow().replace(tzinfo = pytz.utc))

scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)
	
#scheduler.add_job(fetch_data, 'interval', minutes=1)
scheduler.add_job(fetch_amfi_data, 'cron', day_of_week='mon-fri', hour=11, minute=41, end_date='2016-12-31')

scheduler.start()

"""

# Exception Handling

from app.mod_bau.exceptions import DatabaseException


@app.errorhandler(DatabaseException)
def handle_database_exception(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404









