def insertion_sort(lst, to_strict):
	for i in range(len(lst)):
		val = lst[i]
		pos = i
		
		while pos > 0 and lst[pos - 1] > val:
			lst[pos] = lst[pos - 1] # shift value
			pos -= 1 # update position
		
		lst[pos] = val
	return lst
