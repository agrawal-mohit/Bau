from app import db

from mongoengine import *
from mongoengine.fields import StringField
from mongoengine.fields import DateTimeField
from mongoengine.queryset import DoesNotExist

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


class Shift(EmbeddedDocument):
	shiftId = IntField()


class Schedule(Document):
	date = DateTimeField(unique=True)
	shift = MapField(DictField())


	def get_shift(today):
		try:
			shift_obj = Schedule.objects(date=today).exclude('id').get().to_mongo().to_dict()
			shift_obj['date'] = shift_obj['date'].strftime("%d-%m-%Y")
			return shift_obj
		except DoesNotExist:
			raise Exception()

	def get_records(start_date, end_date):
		records = []
		docs = Schedule.objects(date__lte=end_date, date__gte=start_date).exclude('id')
		for doc in docs:
			shift_obj = doc.to_mongo().to_dict()
			shift_obj['date'] = shift_obj['date'].strftime("%d-%m-%Y")
			records.append(shift_obj)
		return records

