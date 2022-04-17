# -*- coding: utf-8 -*-

# William Duong, Nathan Whatley
# CPSC 335-01
# 13 April 2022

# This program will find substrings of cities, and sort and merge
# arrays.


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