# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from mongoengine.queryset import DoesNotExist

from app.mod_bau.services import ScheduleGenerator
from app.mod_bau.models import Schedule

import jsonify
from flask import render_template
from app import db
from bson import json_util
import json
import pdb
import datetime
import pdb



# Define the blueprint: 'rec', set its url prefix: app.url/mintwalk/api
mod_bau = Blueprint('bau', __name__, url_prefix='/')


def respond(msg, status=200):
	return json.dumps({
	    "status" : status,
		"data" : msg
	})

def error(errmsg, status=400):
    return json.dumps({
	    "status" : status,
		"error" : errmsg
	})

def parse(original):
	if type(original) is dict:
		new = dict((k.encode('ascii'), parse(v)) for (k, v) in original.items())
	elif isinstance(original, unicode):
		new = original.encode('ascii')
	else :
		new = original
	return new


   
@mod_bau.route('', methods=['GET'])
def index():
	return render_template('index.html')


@mod_bau.route('shift', methods=['GET'])
def shift():
	# Returns today's shift allotments
	today = datetime.datetime.now().date()

	try:
		todays_shift = Schedule.get_shift(today)
	except:
		# Generate a new schedule for the current period if no shifts alloted for today
		schedule = []
		while(not schedule):
			# If the schedule returned is empty in the case of exception, it is calculated again
			schedule = ScheduleGenerator.generate()

		todays_shift = Schedule.get_shift(today)

	return json.dumps(todays_shift)



