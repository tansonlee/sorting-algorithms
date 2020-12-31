import sys
sys.setrecursionlimit(10000000)

def merge_sort(lst, to_strict):
	if len(lst) > 1:
		half_index = len(lst) // 2

		left = lst[:half_index]
		right = lst[half_index:]
 
		left = merge_sort(left, to_strict)
		right = merge_sort(right, to_strict)
 
		# merge left and right
		i = j = k = 0
		while i < len(left) and j < len(right):
		    if to_strict(left[i], right[j]):
		        lst[k] = left[i]
		        i += 1
		    else:
		        lst[k] = right[j]
		        j += 1
		    k += 1
		# Checking if any element was left
		while i < len(left):
		    lst[k] = left[i]
		    i += 1
		    k += 1
 
		while j < len(right):
		    lst[k] = right[j]
		    j += 1
		    k += 1
	return lst
