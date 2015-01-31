#!/usr/bin/env python

__author__ = "Vassilis Harisopulos <https://github.com/VHarisop>"
__version__ = "0.1"

import sys
if sys.version_info < (3, 0):
	reload(sys)
	sys.setdefaultencoding('utf8')
else:
	raw_input = input



#########
std_input = raw_input
READ_SOURCE = 'console'

#########


class ReadError(Exception):

	def __init__(self, raised_from):
		self.msg = raised_from

	def message(self):
		return "ERROR: Not every object is of type {0}".format(self.msg)

	def __str__(self):
		return self.message()

	

	''' custom Exception class with codes to be defined for Read errors '''


class InputError(Exception):

	''' incomplete Exception class similar to ReadError for general input exceptions, such as missing files, etc. '''
	# TO BE IMPLEMENTED 

	def __init__(self, cause, code=0):
		self.msg = cause
		self.code = code

	def message(self):
		if self.code == 0:
			return "INPUT ERROR: {0}".format(self.msg)
		elif self.code == 1: #error code for invalid file input
			return "INPUT ERROR: {0} {1}".format(self.msg, code)


	def __str__(self):
		return self.message()


class FastaReader(object):

        


class Read(object):

	''' custom class for effectively reading numeric types from the standard input '''
	''' better used when it is not instantiated. for example, to read a line of ints: _ints = Read().ints() '''


	def __init__(self, data_string=None, filename=None, file_toggle='r'):

		if data_string == None:
				self.data = std_input()
		else:
				self.data = data_string

		if filename:
				try:
						fd = file.open(filename, file_toggle)
						self.data = fd.readlines()
						fd.close()
				except:
						raise InputError("Opening file", 1)


	def file_lines(self, delimiter=' '):
		''' this function splits each one of the read lines by a given delimiter '''

		return [i.split(delimiter) for i in self.data] #splits every line by a given delimiter
									 #and puts them all to a list


	def line(self, delimiter=' '):
		''' splits a line according to a delimiter '''

		return [i for i in self.data.split(delimiter)] #returns a list of objects of str-type

	
	def ints(self):

		''' reads integers and returns them as a list '''

		try:
			self.temp_data = [int(x) for x in self.data.split()]
			return self.temp_data
		except ValueError:
			print(ReadError("int").message())
		




	def floats(self):

		'''reads floats and returns them as a list '''

		try:
			self.temp_data = [float(x) for x in self.data.split()]
			return self.temp_data

		except ValueError:
			print(ReadError("float").message())

		

	def complex(self):

		''' reads complex numbers and returns them as a list '''

		try:
			self.temp_data = [complex(x) for x in self.data.split()]
			return self.temp_data
		except ValueError:
			print(ReadError("complex").message())


	
	def nums(self):

		''' reads all 3 kinds of numbers and returns them as a list '''
		try:
			self.temp_data = [getnum(x) for x in self.data.split()] #getnum(x) returns either an int, a float, or a complex number
			return self.temp_data
		except ValueError:
			print(ReadError("any type").message())




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


class Write(object):

	def __init__(self, data):
		self.data_to_write = data

	def __init__(self, destination_file, data=None):
		self.data = data
		self.target = destination_file
		self.destination = file.open(self.target, 'w')
		self.destination.write(data)
		self.data = None

	def flush_toFile(self, data=None):
		self.data = data
		self.destination.write(self.data)
		self.data = None

	def close_File(self):
		self.destination.close()
		



#####
def redefine_std_input(source, name=None, mode='r'):

	''' called as # redefine_std_input(file, 'samplefile.txt') to set the standard input to a file '''
	# INCOMPLETE

	if source == "file":
		std_input = open(name, mode).readline	
		READ_SOURCE = 'file' #redefine the global, SOURCE variable

	else:
		std_input = source


		
def getnum(num_string):


	''' parses a numeric type from a given string (num_string) '''
		
	temp = None
	try:
		temp = int(num_string)
	except:
		try:
			temp = float(num_string)
		except:
			temp = complex(num_string)
	
	return temp

	







