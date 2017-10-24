from app import db

from mongoengine import *
from mongoengine.fields import StringField
from mongoengine.fields import DateTimeField
from datetime import datetime
import pdb



class Engineer(Document):
	id          = IntField(primary_key=True)
	name		= StringField(max_length=200)


	def list():
		engineers_list = []
		docs = Engineer.objects()
		for doc in docs:
			engineers_list.append(doc.to_mongo().to_dict())
		return engineers_list



class Schedule(Document):
	date = DateTimeField(unique=True)
	shift = MapField(DictField())


	def get_shift(today):
		shift_obj = Schedule.objects(date=today).exclude('id').get().to_mongo().to_dict()
		shift_obj['date'] = shift_obj['date'].strftime("%d-%m-%Y")
		return shift_obj

	def get_records(today):
		records = []
		pdb.set_trace()
		docs = Schedule.objects(date__lte=today).exclude('id').get()
		for doc in docs:
			shift_obj = doc.to_mongo().to_dict()
			shift_obj['date'] = shift_obj['date'].strftime("%d-%m-%Y")
			records.append(shift_obj)
		return records

