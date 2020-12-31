# Bubble sort using a strict total order

def swap(lst, i1, i2):
	temp = lst[i1]
	lst[i1] = lst[i2]
	lst[i2] = temp
	return lst

def bubble_sort(lst, to_strict):
	swapped = True
	while swapped:
		swapped = False
		for i in range(0, len(lst) - 1):
			if to_strict(lst[i + 1], lst[i]): 
				lst = swap(lst, i, i + 1)
				swapped = True
	return lst
	