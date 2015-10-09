#!/usr/bin/env python 
"""
This is an application built to import a data file, 
and return a object of specific values in JSON format.
"""
# import csv
from sys import argv


def process(filename):
	"""Returns filename data/ information"""
	with open(filename, 'r', 1) as f:
		total = 0.0
		number_of_lines = 0


		column = []
		
		"""
		take out whitespace 
		need to verify that it matches format for id 1, 2, or 3.  
		Anchor on a 5+ digit number that is likely to be the zipcode.  
		Colors and names can be two words which is problematic. 
		"""
		for row in csv.reader(f, delimiter=' ', skipinitialspace=True):   
			data = row[]
			# colors = ['yellow', 'blue', 'gray', 'aqua marine', 'pink', 'red', 'green']
			input_format = 

				"""
				match to a phone number 
				phonePattern = re.compile(r'''
				                # don't match beginning of string, number can start anywhere
				    (\d{3})     # area code is 3 digits (e.g. '800')
				    \D*         # optional separator is any number of non-digits
				    (\d{3})     # trunk is 3 digits (e.g. '555')
				    \D*         # optional separator
				    (\d{4})     # rest of number is 4 digits (e.g. '1212')
				    \D*         # optional separator
				    (\d*)       # extension is optional and can be any number of digits
				    $           # end of string
				    ''', re.VERBOSE)
				phonePattern.search('work 1-(800) 555.1212 #1234').groups()        
				
				phonePattern.search('800-555-1212')                            
				"""

				# Format 1
				if Regex.IsMatch(row([-1] == ^[0-9]{5+}$))
				
				# Example: Lastname, Firstname, (703)-742-0996, Blue, 10013 				
				# Format Number One: Lastname, Firstname, (000)-000-0000, Color, 00000							
				format_one = {
					"color": [-2], 
					"firstname": [1],
					"lastname": [0], 
					"phonenumber": [-3], 
					"zipcode": [-1]
				}

				if Regex.IsMatch(row([3] == ^[0-9]{5+}$))
				# Example Firstname Lastname, Red, 11237, 703 955 0373 
				# Format Number Two: Firstname Lastname, Color, 00000, 000 000 0000
				format_two = {
					"color": [-5], 
					"firstname": [0],
					"lastname": [-6], 
					"phonenumber": [-3:], 
					"zipcode": [-4]
				}

				if Regex.IsMatch(row([2] == ^[0-9]{5+}$))
				# Example Firstname, Lastname, 10013, 646 111 0101, Green
				# Format Number Three: Firstname, Lastname, 00000, 000 000 0000, Color
				format_three = {
					"color": [-1], 
					"firstname": [0],
					"lastname": [-6], 
					"phonenumber": [-4: -6], 
					"zipcode": [-5]
				}

			try:
				data = float(data)

			#Notify if data error
			except ValueError as err: 
				print(err)
			
			else:
				if data != -999999999:
					total += data
					number_of_lines+= 1

	# return total/number_of_lines
	# return data in JSON format 

if __name__ == '__main__': 
	del argv[0]
	if not argv:
		print("Error: need filename arg")
	else:
		filename = argv[0]
		print process(filename)
