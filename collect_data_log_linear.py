from merge_sort import merge_sort
from quick_sort import quick_sort
from tree_sort import tree_sort

from timer import timer

repeats = 3

print("\n")

## Merge Sort
print("MERGE SORT --------------------------------")
intervals = [i for i in range(0, 1200001, 100000)]
timer(intervals, repeats, merge_sort)
print("DONE MERGE SORT\n\n")

## Quick Sort
print("QUICK SORT --------------------------------")
intervals = [i for i in range(0, 1200001, 100000)]
timer(intervals, repeats, quick_sort)
print("DONE QUICK SORT\n\n")

## Tree Sort
print("TREE SORT --------------------------------")
intervals = [i for i in range(0, 1200001, 100000)]
timer(intervals, repeats, tree_sort) 
print("DONE TREE SORT\n\n")