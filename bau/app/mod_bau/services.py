from app.mod_bau.rules import ConsecutiveRule, OneShiftRule
from app.mod_bau.models import Schedule
import random 

class ScheduleGenerator(object):
	# Generates a schedule for a period
	PERIOD_DAYS = 10
	SHIFT_PER_PERIOD = 20
	SHIFT_PER_ENGINEER_PER_PERIOD = 2

	def period_dates():
		this_day = datetime.datetime.now().date()
		period_dates = []

		while (len(period_dates) < (PERIOD_DAYS)):
			if (this_day.strftime("%a") not in ['Sat', 'Sun']):
				period_dates.append(this_day.strftime("%d-%m-%Y"))
			this_day += datetime.timedelta(days=1)

		return period_dates

	def engineers_pool():
		pool = []
		for i in range(SHIFT_PER_ENGINEER_PER_PERIOD):
			pool.append(Engineers.list())
		return pool


	def generate():
		schedule = {}
		candidates_pool = engineers_pool()

		for date in period_dates():
			schedule[date] = {}
			for shift in range(1, SHIFT_PER_PERIOD/PERIOD_DAYS):
				allocated = False
				while(not allocated):
					candidate = random.choice(candidates_pool) # Randomly picking a candidate from the pool
					if (ConsecutiveRule.isValid(candidate.id, date, schedule) & OneShiftRule.isValid(candidate.id, date, shift, schedule )):
						schedule[date][shift] = candidate
						candidates_pool.pop(candidates_pool.index(candidate))
						allocated = True
		
		save(schedule)
		return schedule

	def save(shifts):
		for date,shift in shifts.enumerate():
			schedule = Schedule(date=date,shift=shift)
			schedule.save()

		

