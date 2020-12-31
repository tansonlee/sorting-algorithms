import matplotlib.pyplot as plt
from bubble_sort import bubble_sort

fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_title("Log-Linear Sorting Algorithms")
ax.set_xlabel("Size of List (x10^6)")
ax.set_ylabel("Time to Sort (seconds)")

plt.xlim([0, 2200000])
plt.ylim([0, 25])

# tree sort
tree_xs = [0, 200000, 400000, 600000, 800000, 1000000]
tree_ys = [0, 3.8000361, 8.491945797, 13.66407466, 18.37704976, 24.04617665]
ax.plot(tree_xs, tree_ys, c='tab:blue', label="tree sort")

# merge sort
merge_xs = [0, 200000, 400000, 600000, 800000, 1000000, 1200000, 1400000, 1600000, 1800000]
merge_ys = [0, 2.19821331, 4.558200693, 7.236635641, 9.839362514, 12.42785704, 15.28047712, 18.06919036, 20.61133478, 23.63594839]
ax.plot(merge_xs, merge_ys, c='tab:orange', label="merge sort")

# quick sort
quick_xs = [0, 200000, 400000, 600000, 800000, 1000000, 1200000, 1400000, 1600000, 1800000, 2000000, 2200000]
quick_ys = [0, 1.736195809, 3.483308883, 5.599847451, 7.506726042, 9.975463194, 11.83141063, 13.84929127, 16.37480862, 18.38590514, 20.18996633, 23.07496185]
ax.plot(quick_xs, quick_ys, c='tab:green', label="quick sort")


plt.legend(loc='upper left');
plt.show()