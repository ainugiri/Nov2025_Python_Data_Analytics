import pandas as pd
df = pd.read_excel("NovTraining.xlsx")


print(df["Topic"].str.contains("AWS", case=False,na=False))
print(df[df["Topic"].str.contains("AWS", case=False,na=False)])


print(df.iloc[0:5])
print(df.iloc[[1,2,12,22,23,30]])

print(df.loc[0:20,"Trainer "])