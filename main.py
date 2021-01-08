from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from tree_sort import tree_sort

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

person1 = Person("Laura", 18)
person2 = Person("James", 22)
person3 = Person("Sam", 12)
person4 = Person("Anthony", 18)

people = [person1, person2, person3, person4]

# order people by their age.
# if their age is equal, order by name alphabetically
def strict_total_order(person1, person2):
	if person1.age != person2.age:
		return person1.age < person2.age
	elif person1.name.lower() != person2.name:
		return sorted([person1.name.lower(), person2.name.lower()])[0] == person1.name.lower()
	else: # names and age are equal
		return False # they are equal

sorted_people = tree_sort(people, strict_total_order)

for person in sorted_people:
	print(person.name, end=" ")