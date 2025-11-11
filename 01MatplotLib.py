import matplotlib.pyplot as plt

x = [1,2,3,4,5,6]
y = [12,13,14,16,19,23]


plt.scatter(x,y, marker='o', color='orange', alpha=1, s=200)
plt.scatter(x,y,marker='x',color='black',s=50)
plt.plot(x,y)
plt.show()

