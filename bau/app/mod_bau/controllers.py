# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for




import json
import sys, traceback
import csv
from flask import make_response
from flask import send_file
from flask import render_template
import os
import jinja2
from app import db
from bson import json_util
import json
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


@mod_bau.route('schedule', methods=['GET'])
def index():
	return render_template('index.html')


# # Set the route and accepted methods
# @mod_bau.route('login', methods=['GET'])
# def login():
#     form = SigninForm()
#     return render_template("auth/signin.html", form=form)

# # Set the route and accepted methods
# @mod_bau.route('register', methods=['GET'])
# def register():
#     form = SignupForm()
#     return render_template("auth/signup.html", form=form)





