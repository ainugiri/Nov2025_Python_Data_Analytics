import pandas as pd
df1 = pd.read_excel("./Emp_Dept.xlsx")
df2 = pd.read_excel("./Emp_loc.xlsx")

print(pd.merge(df1,df2,on="e1", how="inner"))
