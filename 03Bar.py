import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
x = [1,2,3,4,5,6]
y = [12,13,14,16,19,23]


plt.bar(x,y,color="orange", edgecolor="black", width=0.2)
plt.show()
plt.barh(x,y)
# plt.plot(x,y)
plt.show()

data = {
    "Age" : [21,22,27,32,37,41],
    "Sal" : [30,32,55,75,105,140]
}

df = pd.DataFrame(data)
plt.bar(df["Age"],df["Sal"])
plt.show()

cities = ["Chennai","Mumbai","Pune"]
sales_2023=[120,110,105]
sales_2024=[78,92,88]
sales_2025=[108,111,114]
year=[2023,2024,2025]

x = np.arange(len(cities))
width=0.35
plt.bar(x - width/2,sales_2023,width,label="2023")
plt.bar(x,sales_2024,width,label="2024")
plt.bar(x + width/2,sales_2025,width,label="2025")
plt.show()

plt.plot(year, sales_2023, marker='o', label="2023")
plt.plot(year, sales_2024, marker='o', label="2024")
plt.plot(year, sales_2025, marker='o', label="2025")
plt.title("Sales data")
plt.xlabel("Year")
plt.ylabel("Sales in crores")
plt.show()


