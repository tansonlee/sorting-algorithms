def swap(lst, i1, i2):
	temp = lst[i1]
	lst[i1] = lst[i2]
	lst[i2] = temp

def get_min_index(lst, to_strict):
	record_index = 0
	for i in range(len(lst)):
		if to_strict(lst[i], lst[record_index]):
			record_index = i
	return record_index

def selection_sort(lst, to_strict):
	for i in range(len(lst)):
		min_index = get_min_index(lst[i:], to_strict)
		swap(lst, i, min_index + i)
	return lst
