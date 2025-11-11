import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
data = {
    "Age" : [21,22,27,32,37,41],
    "Sal" : [30,32,55,75,105,140]
}

# df = pd.DataFrame(data)
# df.plot(kind="scatter",x="Age",y="Sal")
# plt.show()

data = {
    "sep_l" : [1.2, 1.1, 1.3, 1.4, 3.4, 3.5, 3.4, 3.55, 3.6,5.3,5.4,5.5],
    "sep_w" : [3.5, 3.43, 3.56, 3.62, 8, 8.2, 8, 8.2, 8.1,5.5,5.6,5.7],
    "species": ["A","A","A","X","X","Y","X","X","X","X","Y","Y"]
}


df = pd.DataFrame(data)
sns.scatterplot(x="sep_l",y="sep_w",hue="species",data=df)
plt.title("Seaborn lib, scatter")
plt.show()



# irisdata = load_iris()
# iris = pd.DataFrame(irisdata, columns=irisdata.feature_names)
# iris["species"] =irisdata.target
# print(iris)

# sns.scatterplot(x="sepal length (cm)",y="sepal width (cm)",hue="species",data=iris)
# plt.show()

