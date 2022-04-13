# -*- coding: utf-8 -*-

# William Duong, Nathan Whatley
# CPSC 335-01
# 13 April 2022

# This program will find substrings of cities, and sort and merge
# arrays.


# 3B

array_1 = [[2,5,9,21], [-1,0,2], [-10,81,121], [4,6,12,20,150]]
array_2 = [[10,17,18,21,29], [-3,0,3,7,8,11], [81,88,121,131], [9,11,12,19,29]]
array_3 = [[-4,-2,0,2,7], [4,6,12,14], [10,15,25], [5,6,10,20,24]]

left_array = array_1[0]

right_array = array_1[1]
sub_array = []



i = 0
j = 0
k = 0
while i < len(left_array) and j < len(right_array):

	if(left_array[k] < right_array[i]):
		sub_array[k] = left_array[i]
		i =+ 1
	else:
		sub_array[k] = right_array[j]
		j += 1
	k += 1
print(sub_array)	