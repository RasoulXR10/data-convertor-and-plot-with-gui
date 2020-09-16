import matplotlib.pyplot as plt

list_tuple = [(1, 20), (2, 25), (3, 30), (4, 35), (5, 40),
              (6, 45), (7, 50), (8, 55), (9, 60), (10, 65)]

x = [i[0] for i in list_tuple]
y = [i[1] for i in list_tuple]
plt.plot(x, y)
plt.show()
