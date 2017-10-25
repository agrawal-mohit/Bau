from app.mod_bau.rules import ConsecutiveRule, OneShiftRule, OneDayPerPeriodRule
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
			datekey = date.strftime("%d-%m-%Y")

			schedule[datekey] = {}
			last_period_schedule = ScheduleGenerator.get_last_period_schedule(date) # Returns the schedule of last PERIOD_DAYS days 
			for shift in range(1, 1+int(SHIFT_PER_PERIOD/PERIOD_DAYS)):
				allocated = False
				attempts = 0
				while(not allocated):
					candidate = random.choice(candidates_pool) # Randomly picking a candidate from the pool
					print("Candidate : ", candidate)
					if (ConsecutiveRule.isValid(candidate['_id'], date, schedule) & OneShiftRule.isValid(candidate['_id'], date, shift, schedule) & (initializing | OneDayPerPeriodRule.isValid(candidate['_id'], date, last_period_schedule))):
						schedule[datekey][str(shift)] = candidate
						candidates_pool.pop(candidates_pool.index(candidate))
						allocated = True
						print("Alloted!")
					else:
						# The above algorithm will not return a valid allotment in case of an exception where
						# 1. a candidate is not alloted till the second last day of the period OR
						# 2. no candidate meets the criteria in as many attempts as there are shifts in a period (this is an arbitrary but reasonable limit)
						# In this case the rules are likely to be not satisfied and the generator is ran again
						attempts += 1
						print(attempts)
						if (attempts == SHIFT_PER_PERIOD*5):
							return []
		
		for date,shift in schedule.items():
			try:
				entry = Schedule(date=datetime.datetime.strptime(date, "%d-%m-%Y"),shift=shift)
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
		period_start_date = min(ScheduleGenerator.last_period_dates())
		period_schedule = Schedule.get_records(start_date=period_start_date, end_date=end_date)
		return json.dumps(period_schedule)

