from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort

from timer import timer

repeats = 3

# to 20sec each

print("\n")

## Bubble Sort
print("BUBBLE SORT --------------------------------")
intervals = [i for i in range(0, 8001, 1000)]
timer(intervals, repeats, bubble_sort)
print("DONE BUBBLE SORT\n\n")

## Insertion Sort
print("INSERTION SORT --------------------------------")
intervals = [i for i in range(0, 17001, 1000)]
timer(intervals, repeats, insertion_sort)
print("DONE INSERTION SORT\n\n")

## Selection Sort
print("SELECTION SORT --------------------------------")
intervals = [i for i in range(0, 14001, 1000)]
timer(intervals, repeats, selection_sort)
print("DONE SELECTION SORT\n\n")