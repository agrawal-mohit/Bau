
from app.mod_bau.models import Engineers 

class CandidatePool(object):
	# Factory to generate a pool of cadidates to allot support shifts

	@classmethod
	def create(self, shiftsPerEngineerPerPeriod):
		pool = []
		for i in range(shiftsPerEngineerPerPeriod):
			pool.append(Engineers.list())
		return pool
