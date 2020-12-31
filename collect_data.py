from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from tree_sort import tree_sort

from timer import timer

repeats = 3

print("\n")

## Bubble Sort
print("BUBBLE SORT --------------------------------")
intervals = [i for i in range(0, 7001, 1000)]
timer(intervals, repeats, bubble_sort)
print("DONE BUBBLE SORT\n\n")

## Insertion Sort
print("INSERTION SORT --------------------------------")
intervals = [i for i in range(0, 15001, 1000)]
timer(intervals, repeats, insertion_sort)
print("DONE INSERTION SORT\n\n")

## Selection Sort
print("SELECTION SORT --------------------------------")
intervals = [i for i in range(0, 12001, 1000)]
timer(intervals, repeats, selection_sort)
print("DONE SELECTION SORT\n\n")

## Merge Sort
print("MERGE SORT --------------------------------")
intervals = [i for i in range(0, 200001, 10000)]
timer(intervals, repeats, merge_sort)
print("DONE MERGE SORT\n\n")

## Quick Sort
print("QUICK SORT --------------------------------")
intervals = [i for i in range(0, 200001, 10000)]
timer(intervals, repeats, quick_sort)
print("DONE QUICK SORT\n\n")

## Tree Sort
print("TREE SORT --------------------------------")
intervals = [i for i in range(0, 200001, 10000)]
timer(intervals, repeats, tree_sort) 
print("DONE TREE SORT\n\n")