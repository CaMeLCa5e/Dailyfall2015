#!/usr/bin/env python 
"""
This is an application built to import a data file, 
average and return a specific value.
"""
import csv
from sys import argv

class RoloFunction(object):
	"""Iterate through process for RoloFunction"""
	def __init__(self, input_format= []):
		# super(RoloFunction, self).__init__()
		self.input_format= input_format
		self.error_lines= []
		self.rolodex_data= []

		self.formats = { 'format_one': ('lastname', 'firstname', 'phonenumber', 'color', 'zipcode')
						 'format_two': ('firstname', 'lastname', 'color', 'zipcode', 'phonenumber')
						 'format_three': ('firstname', 'lastname', 'zipcode', 'phonenumber', 'color')
					}
				# Format 1
				# if Regex.IsMatch(row([-1] == ^[0-9]{5+}$))
				# Example: Lastname, Firstname, (703)-742-0996, Blue, 10013 				
				# Format Number One: Lastname, Firstname, (000)-000-0000, Color, 00000							
				format_one = {
					"color": [-2], 
					"firstname": [1],
					"lastname": [0], 
					"phonenumber": [-3], 
					"zipcode": [-1]
				}

				# if Regex.IsMatch(row([3] == ^[0-9]{5+}$))
				# Example Firstname Lastname, Red, 11237, 703 955 0373 
				# Format Number Two: Firstname Lastname, Color, 00000, 000 000 0000
				format_two = {
					"color": [-5], 
					"firstname": [0],
					"lastname": [-6], 
					"phonenumber": [-3:], 
					"zipcode": [-4]
				}

				# if Regex.IsMatch(row([2] == ^[0-9]{5+}$))
				# Example Firstname, Lastname, 10013, 646 111 0101, Green
				# Format Number Three: Firstname, Lastname, 00000, 000 000 0000, Color
				format_three = {
					"color": [-1], 
					"firstname": [0],
					"lastname": [-6], 
					"phonenumber": [-4: -6], 
					"zipcode": [-5]
				}

		}
		
	def process(filename):
		"""Returns the average value from the last column of filename"""
		with open(filename, 'r', 1) as f:
			# total = 0.0
			number_of_lines = 0

			# column = []
			
			#split by pipes, and take out whitespace
			for row in csv.reader(f, delimiter=' ', skipinitialspace=True): 
				data = row  


				print row [1:]
				if row [-1] == 'green':
					print '---'
				else:
					pass

				
				# print data


				# try:
					# data = float(data)
					# return data
				#Notify if data error
				# except ValueError as err: 
				# 	print(err)
				
				# else:
				# 	if data != -999999999:
				# 		total += data
				# 		number_of_lines+= 1


if __name__ == '__main__': 
	del argv[0]
	if not argv:
		print("Error: need filename arg")
	else:
		filename = argv[0]
		print process(filename)
