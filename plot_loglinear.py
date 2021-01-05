import matplotlib.pyplot as plt
from bubble_sort import bubble_sort

fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_title("Log-Linear Sorting Algorithms")
ax.set_xlabel("Size of List (millions)")
ax.set_ylabel("Time to Sort (seconds)")

plt.xlim([0, 1_200_000])
plt.ylim([0, 30])

# tree sort
tree_xs = [i for i in range(0, 1200001, 100000)]
tree_ys = [0, 1.683524319, 3.729761699, 5.94639734, 8.347433502, 10.6636016, 13.59064997, 16.43681105, 18.44009485, 21.17799396, 23.52285662, 25.92722007, 28.12285263]
ax.plot(tree_xs, tree_ys, c='tab:blue', label="tree sort")

# merge sort
merge_xs = [i for i in range(0, 1200001, 100000)] 
merge_ys = [0, 1.046712573, 2.126425521, 3.352789448, 4.549149088, 5.842821486, 7.118824212, 8.372655427, 9.701503793, 11.00951728, 12.34090666, 13.72678694, 15.12826867]
ax.plot(merge_xs, merge_ys, c='tab:red', label="merge sort")

# quick sort
quick_xs = [i for i in range(0, 1200001, 100000)]
quick_ys = [0, 0.763579506, 1.65103401, 2.612733445, 3.510366021, 4.539139283, 5.486257902, 6.940136587, 8.01832586, 9.079331731, 10.23489226, 11.12143757, 11.81653376]
ax.plot(quick_xs, quick_ys, c='tab:green', label="quick sort")


plt.legend(loc='upper left');
plt.show()