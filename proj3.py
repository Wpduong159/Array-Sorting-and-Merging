# -*- coding: utf-8 -*-

# William Duong, Nathan Whatley
# CPSC 335-01
# 13 April 2022

# This program will find substrings of cities, and sort and merge
# arrays.


def algorithm1():
	"""This function will find substrings of one long string"""

	# Inputs
	array1a = "sanoaklandrialtofullertonmarcolongchinocoronamodestoclovissimithousand"
	array1b = ["oakland", "modesto", "clovis", "corona"]
	output1a = []
	output1b = []

	array2a = "polmonafremontrialtofullertonmarcolongfresnochinoclovissimisalinas"
	array2b = ["fullerton", "chino", "fremont", "fresno"]
	output2a = []
	output2b = []

	array3a = "torranceoaklandrialtomarcooxnardchinofresnoirvineclovissimiorange"
	array3b = ["oxnard", "irvine", "orange", "marco"]
	output3a = []
	output3b = []


	# Finding target substrings
	for city in array1b:
		if city in array1a:
			output1a.append(array1a.find(city))
			output1b.append(city)
	output1b = [x for _, x in sorted(zip(output1a, output1b))]
	output1a.sort()


	for city in array2b:
		if city in array2a:
			output2a.append(array2a.find(city))
			output2b.append(city)
	output2b = [x for _, x in sorted(zip(output2a, output2b))]
	output2a.sort()


	for city in array3b:
		if city in array3a:
			output3a.append(array3a.find(city))
			output3b.append(city)
	output3b = [x for _, x in sorted(zip(output3a, output3b))]
	output3a.sort()


	# Algorithm 1 output
	print("Output_order_1 = {}".format(output1a))
	print("Output_array_1 = {}\n".format(output1b))

	print("Output_order_2 = {}".format(output2a))
	print("Output_array_2 = {}\n".format(output2b))

	print("Output_order_3 = {}".format(output3a))
	print("Output_array_3 = {}\n".format(output3b))



if __name__ == '__main__':
	"""Main function"""

	algorithm1()