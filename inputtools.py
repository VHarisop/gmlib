#!/usr/bin/env python

__author__ = "Vassilis Harisopulos <https://github.com/VHarisop>"
__version__ = "0.1"



#########
std_input = raw_input
#########


class ReadError(Exception):

	def __init__(self, raised_from):
		self.msg = raised_from

	def message(self):
		return "ERROR: Not every object is of type {0}".format(self.msg)

	

	''' custom Exception class with codes to be defined for Read errors '''


class InputError(Exception):

	''' incomplete Exception class similar to ReadError for general input exceptions, such as missing files, etc. '''
	# TO BE IMPLEMENTED 


class Read(object):

	''' custom class for effectively reading numeric types from the standard input '''


	def __init__(self):
		self.data = std_input()
		self.temp_data = self.data

	def __init__(self, data_string):
		self.data = data_string

	
	def ints(self):

		''' reads integers and returns them as a list '''

		try:
			self.temp_data = [int(x) for x in self.data.split()]
		except ValueError:
			print(ReadError("int").message())
		
		return self.temp_data




	def floats(self):

		'''reads floats and returns them as a list '''

		try:
			self.temp_data = [float(x) for x in self.data.split()]
		except ValueError:
			print(ReadError("float").message())

		return self.temp_data
		

	def complex(self):

		''' reads complex numbers and returns them as a list '''

		try:
			self.temp_data = [complex(x) for x in self.data.split()]
		except ValueError:
			print(ReadError("complex").message())

		return self.temp_data


	def ints_toTuple(self):
		return tuple(self.ints())


	def ints_toSet(self):
		return set(self.ints())


	def floats_toTuple(self):
		return tuple(self.floats())


	def floats_toSet(self):
		return set(self.floats())


	def complex_toTuple(self):
		return tuple(self.complex())


	def complex_toSet(self):
		return set(self.complex())




#####
def redefine_std_input(source, name=None, mode='r'):

	''' called as # redefine_std_input(file, 'samplefile.txt') to set the standard input to a file '''
	# INCOMPLETE

	if source == "file":
		std_input = open(name, mode).readline

	else:
		std_input = source


		


	







