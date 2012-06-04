from itertools import *
from math import sqrt


class gm_Set(object):

	def __init__(self, iterable):
		self.iterable = iterable
	

	def show(self):
		'''returns the set'''
		return self.iterable
	
	def powerset(self):
		'''returns the iterator that supplies the powerset'''
		s = list(self.iterable)
		return chain.from_iterable((combinations(s, r) for r in range(len(s)+1)))

		
	def powerset_list(self):
		'''returns a list with the powerset'''
		s = list(self.powerset())

	
	def permutation_list(self, num):
		'''returns a list with all the set permutations'''
		s = list(permutations(self.iterable, num))
		return s

	
	def first(self, times):
		return list(islice(self.iterable, times))


	def nth(self, num, default=None):
		''' return the n-th element of the set '''

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

		self.obs = obs #stats list

		self._average = self.average()
		self._standard_deviation = self.standard_deviation()
		self._mean_deviation = self.mean_deviation()


	def __init__(self, obs, _gmfile):

		self.gmfile = _gmfile #the gm-type formatted file with the stat list

		self.obs = _gmfile.get_stats() #get the stats list from the gm_File

		self._average = self.average()
		self._standard_deviation = self.standard_deviation()
		self._mean_deviation = self.mean_deviation()

	
	def average(self):
		return float(sum(self.obs))/len(self.obs)


	def total(self):
		return sum(self.obs)


	def maximum(self):
		return max(self.obs)

	def minimum(self):
		return min(self.obs)


	def standard_deviation(self):
		'''returns the standard deviation of the stats'''
		p_sum = sum([(i - self._average)**2 for i in self.obs])
		dev = sqrt((float(p_sum))/len(self.obs))
		return dev

	def mean_deviation(self):
		'''returns the mean deviation of the stats'''
		m_dev = float(self._standard_deviation) / (sqrt(len(self.obs)))
		return m_dev


	def results(self, mode=None):
		if mode == None:
			print("Average: {0} \nStandard Deviation: {1} \nMean Deviation: {2}".format(self._average, self._standard_deviation, self._mean_deviation))
		elif mode == "list":
			return [self._average, self._standard_deviation, self._mean_deviation]
		elif mode == "dict":
			return {'Average': self._average, 'Standard Deviation': self._standard_deviation, 'Mean Deviation': self._mean_deviation}


	def save_stats(self, name):
		'''saves the stats to a gm_File'''
		temp_file = open(name, 'w')
		for item in self.obs:
			temp_file.write("{0} \n".format(str(item))) # save the statistics one at a line. 
								    #This can be easily modified so that multiple stats 
								    #with the same tag can be saved on one line
		temp_file.flush()
		temp_file.close()

		return gm_File(name, "stats") #returns the coresponding gm_File 

	def save_measures(self, name):
		'''saves the measures(avg, std_dev, mean_dev) to a gm_File'''
		temp_file = open(name, 'w')
		temp_file.write("Average {0}\n".format(self._average))
		temp_file.write("Standard_Deviation {0}\n".format(self._standard_deviation))
		temp_file.write("Mean_Deviation {0}\n".format(self._mean_deviation))
		temp_file.flush()
		temp_file.close()

		return gm_File(name, "measures") #return the coresponding gm_File




class gm_Interactive(object):

	def __init__(self, input_source=raw_input):
		self.input_source = input_source


	def Ints(self): 
		self.intlist = [int(item) for item in self.input_source().split()]
		return self.intlist

	def Floats(self):
		self.floatlist = [float(item) for item in self.input_source().split()]
		return self.floatlist

	def MakeList(self, *args):
		return list(args)

	def MakeDict(self, *d_args):
		return dict(d_args)

	def Evaluate(self, expression):
		return eval(expression)

	
class gm_File(object):

	def __init__(self, filepath, datatype):
		self.filepath = filepath
		self.datatype = datatype


	def get_stats(self):
		if self.datatype == "stats":
			temp = open(self.filepath, "r")
			line_list = temp.readlines()
			stat_list = [float(i.split()[0]) for i in line_list] #i.split() gives us the observation value in a list
			                                                     #it's the zero-indexed item. To choose it, we simply choose the index 0.
			
			return stat_list


		elif self.datatype == "measures":
			temp = open(self.filepath, "r")
			line_list = temp.readlines()
			measure_list = [i.split() for i in line_list]
			results = {}
			for item in measure_list:
				results[item[0]] = float(item[1]) 
				#for example, if item[0] == "Average", and item[1] = 12 then results{'Average': 12.0}

			return results


