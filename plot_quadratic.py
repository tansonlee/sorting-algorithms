import matplotlib.pyplot as plt
from bubble_sort import bubble_sort

fig = plt.figure()
ax = fig.add_subplot(111)

# bubble sort
bubble_xs = [100, 200, 600, 1000, 2000, 4000]
bubble_ys = [0.002388906, 0.011671768, 0.103704497, 0.307285144, 1.238294377, 5.050942825]
ax.plot(bubble_xs, bubble_ys, c='tab:cyan', label="bubble sort")

# insertion sort
insertion_xs = [100, 200, 600, 1000, 2000, 4000]
insertion_ys = [0.000617657, 0.002079222, 0.022328386, 0.069712827, 0.283719646, 1.096839277]
ax.plot(insertion_xs, insertion_ys, c='tab:red', label="insertion sort")

# selection sort
selection_xs = [100, 200, 600, 1000, 2000, 4000]
selection_ys = [0.000617657, 0.002079222, 0.022328386, 0.069712827, 0.283719646, 2.096839277]
ax.plot(selection_xs, selection_ys, c='tab:purple', label="selection sort")

plt.legend(loc='upper left');
plt.show()