

import datetime

class ConsecutiveRule(object):

	@staticmethod
	def isValid(candidateId, date, schedule):

		last_day = (date + datetime.timedelta(days=-1))
		if (last_day.strftime("%a") not in ['Sun']):
			previous_day = (date + datetime.timedelta(days=-1)).strftime("%d-%m-%Y")
		else :
			previous_day = (date + datetime.timedelta(days=-3)).strftime("%d-%m-%Y")

		if(date == datetime.datetime.now().date()):
			# This is the starting of the defined period so allotment is valid
			print("consecutive :  pass1 ")
			return True
		elif ((schedule[previous_day].get('1', {'_id' : ''})['_id'] != candidateId ) & (schedule[previous_day].get('2', {'_id' : ''})['_id'] != candidateId )):
			# This candidate did not have a shift previous day so allotment is valid
			print("consecutive :  pass2 ")
			return True

		print("consecutive :  fail ")

		return False



class OneShiftRule(object):

	@staticmethod
	def isValid(candidateId, date, shift, schedule):

		this_day = date.strftime("%d-%m-%Y")
		
		if (shift ==1):
			# This is the first shift so allotment is valid
			print("oneshift :  pass 1")
			return True
		if (schedule[this_day]['1']['_id'] == candidateId):
			print("oneshift :  fail ")
			return False
		else:
			print("oneshift :  pass 2`")
			return True

