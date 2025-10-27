import matplotlib.pyplot as plt
import numpy as np

x = np.array(["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10"])
y = np.array([80, 100, 62, 76, 244, 33, 17, 998, 999, 10])

print(np.mean(y))
print(np.median(y))
print(np.std(y))

plt.xlabel("Courses")
plt.ylabel("grades")

#line chart
plt.plot(x, y)
plt.show()

#pie chart
mylabels = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10"]
plt.pie(y, labels=mylabels)
plt.show()

x = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

print(np.mean(y))
print(np.median(y))
print(np.std(y))

plt.xlabel("1")
plt.ylabel("2")

#linechart
plt.plot(x, y)
plt.show()

#piechart
mylabels = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10"]
plt.pie(y, labels=mylabels)
plt.show()

#scatterplot
plt.scatter(x,y)
plt.show()