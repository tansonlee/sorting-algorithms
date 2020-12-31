import matplotlib.pyplot as plt
from bubble_sort import bubble_sort

fig = plt.figure()
ax = fig.add_subplot(111)


a = [100, 500 ,1000 ,2000 ,4000 ,7000 ,10000 ,12000 ,14000]
b = [0.002765739 ,0.071294508 ,0.323518605 ,1.266604481 ,5.101739018 ,16.09336063 ,32.73350096 ,46.0904132 ,63.39401424]

c = [100 , 500 , 1000 , 2000 , 4000 , 7000 , 10000 , 14000 , 16000 , 20000 , 30000 , 50000 , 120000]

d = [0.000262963 ,0.001877218 ,0.004119136 ,0.010091998 ,0.031713743 ,0.040488318 ,0.063451067 ,0.087159459 ,0.10684712 ,0.138434215 ,0.220469253 ,0.376308809 ,0.95804072]

# ax.scatter(bubble_xs, bubble_ys, s=20, c='b', marker="o", label='bubble sort')
ax.plot(a, b, c='b', label="bubble")
ax.plot(c, d, c='r', label="quick")

# bubble sort
bubble_xs = [100, 200, 600, 1000, 2000, 4000]
bubble_ys = [0.002388906, 0.011671768, 0.103704497, 0.307285144, 1.238294377, 5.050942825]

bubble_fit_xs = [x for x in range(0, 5000, 100)]
bubble_fit_ys = [(0.0000003212 * x * x) - (0.00002308 * x) + 0.00323 for x in bubble_fit_xs]

# ax.scatter(bubble_xs, bubble_ys, s=20, c='b', marker="o", label='bubble sort')
# ax.plot(bubble_fit_xs, bubble_fit_ys, c='b')

# insertion sort
insertion_xs = [100, 200, 600, 1000, 2000, 4000]
insertion_ys = [0.000617657, 0.002079222, 0.022328386, 0.069712827, 0.283719646, 1.096839277]

insertion_fit_xs = [x for x in range(0, 5000, 100)]
insertion_fit_ys = [(0.00000006662 * x * x) + (0.000008673 * x) - 0.003274 for x in insertion_fit_xs]

# ax.scatter(insertion_xs, insertion_ys, s=20, c='r', marker="o", label='insertion sort')
# ax.plot(insertion_fit_xs, insertion_fit_ys, c='r')


plt.legend(loc='upper left');
plt.show()