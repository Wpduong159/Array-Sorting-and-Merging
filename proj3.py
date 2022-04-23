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


# 3B
def merger(left, right):

	sub_array = [None] * (len(left) + len(right))
	
	i = 0
	j = 0
	k = 0
	while i < len(left) and j < len(right):
		
		if(left[i] < right[j]):
			sub_array[k] = left[i]
			i += 1
			k += 1

		else:
			sub_array[k] = right[j]
			j += 1
			k += 1

	while i < len(left):
			sub_array[k] = left[i]
			i += 1
			k +=1

	while j < len(right):
			sub_array[k] = right[j]
			j += 1
			k += 1
	return(sub_array)

  

if __name__ == '__main__':
	"""Main function"""

	algorithm1()

	array_1 = [[2,5,9,21], [-1,0,2], [-10,81,121], [4,6,12,20,150]]
	array_2 = [[10,17,18,21,29], [-3,0,3,7,8,11], [81,88,121,131], [9,11,12,19,29]]
	array_3 = [[-4,-2,0,2,7], [4,6,12,14], [10,15,25], [5,6,10,20,24]]


	print("Pre-merged Example Arrays:")
	print('{}\n{}\n{}'.format(array_1, array_2,array_3))
	print("\nMerged Arrays")


	sorted_1 = merger(array_1[0],array_1[1])
	sorted_2 = merger(array_1[2], array_1[3])
	sorted_3 = merger(sorted_1, sorted_2)

	print(sorted_3)

	sorted_1 = merger(array_2[0],array_2[1])
	sorted_2 = merger(array_2[2], array_2[3])
	sorted_3 = merger(sorted_1, sorted_2)

	print(sorted_3)
	sorted_1 = merger(array_3[0],array_3[1])
	sorted_2 = merger(array_3[2], array_3[3])
	sorted_3 = merger(sorted_1, sorted_2)

	print(sorted_3)