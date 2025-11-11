import matplotlib.pyplot as plt
city=["Chennai","Pune","Mumbai","Begaluru"]
noofemp =[12000,14000,6000,5000]
plt.pie(noofemp,labels=city)
plt.title("Distribution of Employees")
plt.show()