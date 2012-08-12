#!/usr/bin/env python

from itertools import *
from math import sqrt
import sys


__author__ = "Vassilis Harisopulos <https://github.com/VHarisop>"
__version__ = "0.1.9"


if sys.version_info < (3,0):
	reload(sys)
	sys.setdefaultencoding('utf8')
else:
	raw_input = input


class Error(Exception):

	def __init__(self, msg):
		self.msg = msg
	
	def __str__(self):
		return self.msg

class gm_Set(object):


	def __init__(self, iterable):
		self.iterable = iterable

	
	def __str__(self):
		return "gm_Set: {0}".format(self.iterable)

	
	def __repr__(self):
		
		return "gm_Set: {0}".format(self.iterable)


	def __add__(self, other_set):

		''' This function is equivalent to self UNION other 
		    It appends the iterable of the 2nd set to that of the first
		    and then eliminates duplicates '''

		res_list = list(set(self.iterable + other_set.iterable)) #set(_list) eliminates duplicates in a list

		return gm_Set(res_list)

	def __sub__(self, other_set):

		''' This function is equivalent to the EXCLUSION of the 2nd
		    from the first set. It is implemented by creating a new set
		    using only the elements of the 1st set that are not in the 2nd'''
		
		res_list = []
		
		for element in self.iterable:
			if element not in other_set.iterable:
				res_list.append(element)


		return gm_Set(res_list)

	def Intersection(self, other_set):
		
		
		''' This function is equivalent to the INTERSECTION of
		    the 1st and 2nd set. '''

		res_list = []
		for element in self.iterable:
			if element in other_set.iterable:
				res_list.append(element)

		return gm_Set(res_list)

	
	def __eq__(self, other):

		''' Two gm_Sets are considered equal if they
		    have the same elements as an iterable '''

		return True if self.iterable == other.iterable else False


	def __neq__(self, other):

		return True if self.iterable != other.iterable else False


	def Union(self, other_set):
		
		return self + other_set


	def show(self):
		'''returns the set'''
		return self.iterable


	def powerset(self):
		'''returns the iterator that supplies the powerset'''
		s = list(self.iterable)
		return chain.from_iterable((combinations(s, r) for r in range(len(s)+1)))

		
	def powerset_list(self):
		'''returns a list with the powerset'''
		return list(self.powerset())
		

	
	def permutation_list(self, num):
		'''returns a list with all the set permutations
		   if the num argument is bigger than the length of 
		   the iterable, returns an empty list '''
		
		if num <= len(self.iterable):
			s = list(permutations(self.iterable, num))
		else:
			s = []
		return s

	

	def nth(self, num, default=None):
		''' return the n-th element of the set '''

		count = 0
		if num < len(self.iterable):
			while count < num:
				count += 1

			return self.iterable[count]
		else:
			raise Error('Index out of range')

	def first(self, n):

		''' return the first n elements of the iterable '''

		return list(islice(self.iterable, n))

	def product(self):

		''' this function calculates the product of all the set's elements '''

		prod = 1
		for element in self.iterable:
			prod *= element
		return prod



class gm_Statistics(object):

	def __init__(self, obs):

		self.obs = obs #stats list

		self.gmfile = None

		self._average = self.average()
		self._standard_deviation = self.standard_deviation()
		self._mean_deviation = self.mean_deviation()


	def __init__(self, obs, _gmfile):

		self.gmfile = _gmfile #the gm-type formatted file with the stat list

		self.obs = _gmfile.get_stats() #get the stats list from the gm_File

		self._average = self.average()
		self._standard_deviation = self.standard_deviation()
		self._mean_deviation = self.mean_deviation()


	def __eq__(self, other):
		if (self.obs == other.obs) and (self.gmfile == other.gmfile) \
			and (self._average == other._average) \
			and (self._standard_deviation == other._standard_deviation) \
			and (self._mean_deviation == other._mean_deviation):
				return True
		else:
			return False

	def __neq__(self, other):
		if self == other:
			return False
		else:
			return True

	
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


	def __eq__(self, other):
		return (True if self.input_source == other.input_source else False)

	def __neq__(self, other):
		return (False if self.input_source == other.input_source else True)
	

	def Ints(self): 
		return [int(item) for item in self.input_source().split()]
		

	def Floats(self):
		return [float(item) for item in self.input_source().split()]
		

	def MakeList(self, *args):
		return list(args)

	def MakeDict(self, **d_args):
		return dict(d_args)

	def Evaluate(self, expression):
		return eval(expression)

	def MakeDict(self, arg_list, parameter_list):

		''' this function takes an argument and a parameter list
		    and creates an appropriate dictionary. It raises an error
		    if there are more parameters than arguments. 
		    
		    If there are more arguments than parameters, the exceeding ones
		    are automatically mapped to None value. '''


		tmp = {}
		diff = len(arg_list) - len(parameter_list)
		if diff < 0:
			raise Error("too many parameters")
		else:
			while diff > 0:
				parameter_list.append(None) #if there are any missing values in the parameters
							    #auto complete the par_list with None's

				diff -= 1

		for count in range(0, len(arg_list)):
			tmp[arg_list[count]] = parameter_list[count] #map the parameters to the arguments

		return tmp

	
class gm_File(object):

	def __init__(self, filepath, datatype):
		self.filepath = filepath
		self.datatype = datatype

	
	
	def __eq__(self, other):
		
		''' two gm_File objects are considered equal if they have the same datapath and datatype '''

		return True if ((self.filepath == other.filepath) and (self.datatype == other.datatype)) else False

	def __neq__(self, other):

		return False if ((self.filepath == other.filepath) and (self.datatype == other.datatype)) else True


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


class error(Exception): pass



class gm_Stack(object):

	def __init__(self, start=[]):
		self.stack = []
		for item in start:
			self.push(item)

	def __eq__(self, other):

		''' two gm_Stacks are considered equal if the have the same objects in the "stack" field '''
		
		return True if self.stack == other.stack else False


	def __neq__(self, other):
		
		return False if self.stack == other.stack else True

	def push(self, obj):
		self.stack.append(obj)

	def pop(self):
		if not self.stack: raise error('underflow')
		return self.stack.pop()

	def top(self):
		if not self.stack: raise error('underflow')
		return self.stack[-1]

	def empty(self):
		return not self.stack

	def __len__(self):
		return len(self.stack)

	def __getitem__(self, offset):
		return self.stack[offset]

	def __repr__(self):
		return '[Stack: %s]' % self.stack


class gm_Counting(object):


	def __init__(self, elements=[]):

		''' creates a class for counting tasks (discrete math) 
		    with an optional list of elements '''

		self.elements = elements

	def C(self, n, k):

		''' outputs the choice of k out of n elements '''

		n_list = [i for i in range(1, n+1)]
		k_list = [i for i in range(1, k+1)]
		nk_list = [i for i in range(1, n-k+1)]

		common = []
		for element in n_list:
			if element in k_list:
				common.append(element)

		for element in common: #remove common factors between n and k factorials
			n_list.remove(element)
			k_list.remove(element)

		common = []
		for element in n_list:
			if element in nk_list:
				common.append(element)

		for element in common: #remove common factors between n and n-k factorials
			n_list.remove(element)
			nk_list.remove(element)

		for element in [n_list, k_list, nk_list]:
			if element == []:
				element.append(1)

		i = 1
		for element in n_list:
			i *= element

		j = 1
		for element in k_list:
			j *= element

		m = 1
		for element in nk_list:
			m *= element

		return i / (j*m)

	def P(self, n, k):

		''' outputs the number of possible permutations of k out of elements '''

		n_list = [i for i in range(0, n+1)]
		nk_list = [i for i in range(0, n-k+1)]

		common = []
		for element in n_list:
			if element in nk_list:
				common.append(element)

		for element in common: #remove common factors from the fraction
			n_list.remove(element); nk_list.remove(element)

		if n_list == []:
			n_list = [1]

		if nk_list == []:
			nk_list = [1]

		i = 1
		for element in n_list:
			i *= element
		
		j = 1
		for element in nk_list:
			j *= element

		return i / j
