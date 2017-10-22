from app import db

from mongoengine import *
from mongoengine.fields import StringField
from mongoengine.fields import DateTimeField
import datetime



class Engineer(Document):

	id            = IntField(primary_key=True)
	name		= StringField(max_length=200)


class Shift(object):

	def _init__(self, id, engineer):
		self.id = id
		self.engineer = engineer


