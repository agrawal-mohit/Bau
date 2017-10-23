

import datetime

class ConsecutiveRule(object):

	@staticmethod
	def isValid(candidateId, date, schedule):

		previous_day = (date + datetime.timedelta(days=-1)).strftime("%d%m%Y")
			
		if(date == datetime.datetime.now().date()):
			# This is the starting of the defined period so allotment is valid
			return True
		if (schedule[previous_day].shift[1].engineer.id == candidateId & schedule[previous_day].shift[2].enginner.id == candidateId ):
			# This candidate did not have a shift previous day so allotment is valid
			return True
		return False



class OneShiftRule(object):

	@staticmethod
	def isValid(candidateId, date, shift, schedule):

		this_day = date.strftime("%d-%m-%Y")
		
		if (shift ==1):
			# This is the first shift so allotment is valid
			return True
		if (schedule[this_day].shift[1].engineer.id == candidateId):
			return False
		else:
			return True

