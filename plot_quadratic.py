import matplotlib.pyplot as plt
from bubble_sort import bubble_sort

fig = plt.figure()
ax = fig.add_subplot(111)

plt.xlim([0, 19000])
plt.ylim([0, 20])

ax.set_title("Quadratic Time Sorting Algorithms", fontsize=20)
ax.set_xlabel("Size of List (elements)", fontsize=16)
ax.set_ylabel("Time to Sort (seconds)", fontsize=16)

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# bubble sort
bubble_xs = [i for i in range(0, 8001, 1000)]
bubble_ys = [0, 0.299299469, 1.235358564, 2.82793318, 5.07864504, 8.010825149, 11.53334149, 15.96656642, 20.74196788] 
ax.plot(bubble_xs, bubble_ys, c='tab:orange', label="bubble sort")

# selection sort
selection_xs = [i for i in range(0, 14001, 1000)]
selection_ys = [0, 0.09750404, 0.401159441, 0.90952984, 1.640341324, 2.565051534, 3.707070829, 5.096274138, 6.641358541, 8.376500493, 10.33187953, 12.57962561, 14.87646623, 17.83396626, 20.52249039]
ax.plot(selection_xs, selection_ys, c='darkviolet', label="selection sort")

# insertion sort
insertion_xs = [i for i in range(0, 17001, 1000)] 
insertion_ys = [0, 0.065403942, 0.266629282, 0.61332097, 1.10324347, 1.757205955, 2.397509865, 3.39461072, 4.449606701, 5.598851141, 6.923869, 8.333155321, 9.990748035, 11.62466114, 13.71631807, 15.58797276, 17.96887404, 20.47389299]
ax.plot(insertion_xs, insertion_ys, c='tab:cyan', label="insertion sort")

plt.legend(loc='upper left', prop={'size': 14});
plt.show()