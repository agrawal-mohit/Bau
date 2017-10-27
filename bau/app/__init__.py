import os

# Import flask and template operators
from flask import Flask, render_template
from flask_mongoengine import MongoEngine
from flask_bcrypt import Bcrypt
import config

# Define the WSGI application object
app = Flask(__name__ , static_url_path='/static')

app.config.from_object(config.DevelopmentConfig)
db = MongoEngine(app)


bcrypt = Bcrypt(app)
app.debug = True
#CsrfProtect(app)
# Import a module / component using its blueprint handler variable (mod_bau)

from app.mod_bau.controllers       import mod_bau          as bau_module


# Register blueprint(s)
app.register_blueprint(bau_module)


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









