from app.mod_bau.rules import ConsecutiveRule, OneShiftRule
from app.mod_bau.models import Schedule, Engineer
import random, datetime 
import pdb
import json

PERIOD_DAYS = 10
SHIFT_PER_PERIOD = 20
SHIFT_PER_ENGINEER_PER_PERIOD = 2


class ScheduleGenerator(object):
	# Generates a schedule for a period
	

	def period_dates():
		this_day = datetime.datetime.now().date()
		period_dates = []

		while (len(period_dates) < (PERIOD_DAYS)):
			if (this_day.strftime("%a") not in ['Sat', 'Sun']):
				period_dates.append(this_day)
			this_day += datetime.timedelta(days=1)

		return period_dates

	def engineers_pool():
		pool = []
		for i in range(SHIFT_PER_ENGINEER_PER_PERIOD):
			pool.extend(Engineer.list())
		return pool


	def generate():
		schedule = {}
		candidates_pool = ScheduleGenerator.engineers_pool()

		for date in ScheduleGenerator.period_dates():
			schedule[date.strftime("%d-%m-%Y")] = {}
			for shift in range(1, 1+int(SHIFT_PER_PERIOD/PERIOD_DAYS)):
				allocated = False
				while(not allocated):
					candidate = random.choice(candidates_pool) # Randomly picking a candidate from the pool
					if (ConsecutiveRule.isValid(candidate['_id'], date, schedule) & OneShiftRule.isValid(candidate['_id'], date, shift, schedule )):
						schedule[date.strftime("%d-%m-%Y")][str(shift)] = candidate
						candidates_pool.pop(candidates_pool.index(candidate))
						allocated = True
						attempt = 0
					else:
						# The above algorithm will not return a valid allotment in case of an exception where
						# a candidate is not alloted till the second last day of the period
						# In this case the rules cannot be satisfied and the algorithm has to run again
						attempt += 1
						if (attempt == len(candidates_pool)):
							return []

		for date,shift in schedule.items():
			try:
				entry = Schedule(date=datetime.datetime.strptime(date, "%d-%m-%Y"),shift=shift)
				entry.save()
			except Exception as e:
				print(e)

		return json.dumps(schedule)
		

