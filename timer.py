from random import randint
import time

to_strict = lambda x, y : x < y

def generate_random(size):
	return [randint(0, size) for i in range(size)]

def generate_ordered(size):
	return [i for i in range(size)]

def generate_reversed(size):
	return [i for i in reversed(range(size))]

def timer_help(intervals, repeats, generate, sort):
	for i in intervals:
		round_time = []
		for j in range(repeats):
			l = generate(i)
			a = time.perf_counter()
			sort(l, to_strict)
			b = time.perf_counter()
			round_time.append(str(b - a))

		print(str(i) + " " + str(sum([float(r) for r in round_time]) / repeats) + " " + " ".join(round_time))

def timer(intervals, repeats, sort):
	# print("RANDOM")
	s = "size average"
	for i in range(repeats):
		s += " " + "time" + str(i + 1)
	print(s)
	timer_help(intervals, repeats, generate_random, sort)

	# print("-------------------------------------------")
	# print("-------------------------------------------")
	# print("ORDERED")
	# timer_help(intervals, repeats, generate_ordered, sort)

	# print("-------------------------------------------")
	# print("-------------------------------------------")
	# print("REVERSED")
	
	# timer_help(intervals, repeats, generate_reversed, sort)
	# print("-------------------------------------------")
	# print("-------------------------------------------")


def verify_sort(lst, to_strict):
	for i in range(0, len(lst) - 1):
		if to_strict(lst[i + 1], lst[i]):
			return False
	return True