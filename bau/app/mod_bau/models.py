from app import db

from mongoengine import *
from mongoengine.fields import StringField
from mongoengine.fields import DateField
import datetime



class Engineer(Document):
	id          = IntField(primary_key=True)
	name		= StringField(max_length=200)


	def list():
		engineers_list = []
		docs = Engineer.objects.get()
		for doc in docs:
			engineers_list.append(doc.to_mongo().to_dict())
		return engineers_list



class Schedule(Document):
	date = DateField()
	shift = MapField(DictField(ReferenceField('Engineer')))