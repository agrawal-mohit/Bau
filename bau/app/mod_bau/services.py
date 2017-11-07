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


	def generate(initializing=False):
		schedule = {}
		last_period_schedule = []
		candidates_pool = ScheduleGenerator.engineers_pool()

		for date in ScheduleGenerator.period_dates():
			schedule[date.strftime("%d-%m-%Y")] = {}
			for shift in range(1, 1+int(SHIFT_PER_PERIOD/PERIOD_DAYS)):
				allocated = False
				last_period_schedule = ScheduleGenerator.get_last_period_schedule(date) # Returns the schedule of last PERIOD_DAYS days 
				pdb.set_trace()
				while(not allocated):
					
					if (ConsecutiveRule.isValid(candidate['_id'], date, schedule) & OneShiftRule.isValid(candidate['_id'], date, shift, schedule) & (initializing | OneDayPerPeriodRule.isValid(candidate['_id'], date, last_period_schedule))):
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
				entry = Schedule(date=date,shift=shift)
				entry.save()
			except Exception as e:
				print(e)

		return json.dumps(schedule)


	def last_period_dates():

		this_day = datetime.datetime.now().date()
		last_period_dates = []

		while (len(last_period_dates) < (PERIOD_DAYS)):
			if (this_day.strftime("%a") not in ['Sat', 'Sun']):
				last_period_dates.append(this_day)
			this_day += datetime.timedelta(days=-1)

		return last_period_dates
	
	def get_last_period_schedule(end_date):
		pdb.set_trace()
		period_start_date = min(ScheduleGenerator.last_period_dates())
		period_schedule = Schedule.get_records(start_date=period_start_date, end_date=end_date)
		return json.dumps(period_schedule)

