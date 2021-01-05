import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

plt.xlim([0, 200000])
plt.ylim([0, 14])

ax.set_title("Sorting Algorithms", fontsize=20)
ax.set_xlabel("Size of List (elements)", fontsize=16)
ax.set_ylabel("Time to Sort (seconds)", fontsize=16)

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

ax.text(16000, 12, "quadratic time", fontsize=14)
ax.text(140000, 4, "log-linear time", fontsize=14)


# bubble sort
bubble_xs = [i for i in range(0, 7001, 1000)]
bubble_ys = [0, 0.316637417, 1.358731127, 2.918572092, 5.135054007, 7.916411395, 11.24790769, 15.3819458]
ax.plot(bubble_xs, bubble_ys, c='tab:orange', label="bubble sort")

# selection sort
selection_xs = [i for i in range(0, 12001, 1000)]
selection_ys = [0, 0.099181189, 0.40178215, 0.920364322, 1.671383512, 2.589804009, 3.675705712, 5.028809265, 6.432947223, 8.163354792, 10.09395525, 12.36817226, 14.68760056]
ax.plot(selection_xs, selection_ys, c='darkviolet', label="selection sort")

# insertion sort
insertion_xs = [i for i in range(0, 15001, 1000)]
insertion_ys = [0, 0.064237171, 0.261664558, 0.605969898, 1.091974283, 1.700302461, 2.473288389, 3.347905331, 4.393138773, 5.546518625, 6.925221136, 8.335693843, 9.947850786, 11.70808336, 14.07337099, 15.84565998]
ax.plot(insertion_xs, insertion_ys, c='tab:cyan', label="insertion sort")

# tree sort
tree_xs = [i for i in range(0, 200001, 10000)]
tree_ys = [0, 0.11779917, 0.320486946, 0.51255483, 0.70029946, 0.888280582, 1.21822254, 1.365938609, 1.610196918, 1.710637391, 1.934100108, 2.259315929, 2.31000399, 2.460601145, 2.601133243, 2.938564463, 3.088515384, 3.34250221, 3.632307243, 3.808117787, 4.015129969]
ax.plot(tree_xs, tree_ys, c='tab:blue', label="tree sort")

# merge sort
merge_xs = [i for i in range(0, 200001, 10000)]
merge_ys = [0, 0.080031629, 0.178079152, 0.28397666, 0.369154724, 0.467649408, 0.569375168, 0.690644186, 0.80393847, 0.898687919, 1.000035167, 1.113879932, 1.22577674, 1.329018527, 1.460036092, 1.570010371, 1.67354859, 1.800667858, 1.902015928, 2.023224376, 2.133587994]
ax.plot(merge_xs, merge_ys, c='tab:red', label="merge sort")

# quick sort
quick_xs = [i for i in range(0, 200001, 10000)]
quick_ys = [0, 0.059505538, 0.130772246, 0.204778384, 0.274155564, 0.351184084, 0.427069875, 0.514651964, 0.608474146, 0.691340908, 0.766249699, 0.91936481, 1.02935181, 1.135905274, 1.1894149, 1.236783196, 1.286408225, 1.374805473, 1.457546934, 1.567019841, 1.657306287]
ax.plot(quick_xs, quick_ys, c='tab:green', label="quick sort")


plt.legend(loc='upper right', prop={'size': 14});
plt.show()