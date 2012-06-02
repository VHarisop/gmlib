from itertools import *


class gm_Iterable(object):

	def __init__(self, iterable):
		self.iterable = iterable
	

	def show(self):
		return self.iterable
	
	def powerset(self):
		s = list(self.iterable)
		return chain.from_iterable((combinations(s, r) for r in range(len(s)+1)))

		
	def powerset_list(self):
		s = list(self.powerset())

	
	def first(self, times):
		return list(islice(self.iterable, times))


	def nth(self, num, default=None):

		count = 0
		if num < len(self.iterable):
			while count < num:
				count += 1

			return self.iterable[count]
		else:
			return 'Index out of range'

	def first(self, n):
		''' return the first n elements of the iterable '''
		return list(islice(self.iterable, n))


class gm_Statistics(object):

	def __init__(self, obs):
		self.obs = obs
		self._average = self.average()

	
	def average(self):
		return float(sum(self.obs))/len(self.obs)


	def total(self):
		return sum(self.obs)


	def maximum(self):
		return max(self.obs)

	def minimum(self):
		return min(self.obs)

	


class gmRead(object):

	def __init__(self, input_source=raw_input):
		self.input_source = input_source


	def Ints(self):
		self.intlist = [int(item) for item in self.input_source().split()]
		return self.intlist

	def Floats(self):
		self.floatlist = [float(item) for item in self.input_source().split()]
		return self.floatlist

	


