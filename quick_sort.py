import sys
sys.setrecursionlimit(10000000)

def partition(lst, start, end, to_strict):
    pivot = lst[start]
    low = start + 1
    high = end

    while True:
        while (low <= high) and (not to_strict(lst[high], pivot)):
            high = high - 1

        while (low <= high) and (not to_strict(pivot, lst[low])):
            low = low + 1

        if low <= high:
            lst[low], lst[high] = lst[high], lst[low]
        else:
            break

    lst[start], lst[high] = lst[high], lst[start]

    return high

def quick_sort_helper(lst, start, end, to_strict):
    if start >= end:
        return

    p = partition(lst, start, end, to_strict)
    quick_sort_helper(lst, start, p-1, to_strict)
    quick_sort_helper(lst, p+1, end, to_strict)

def quick_sort(lst, to_strict):
	quick_sort_helper(lst, 0, len(lst) - 1, to_strict)
	return lst

