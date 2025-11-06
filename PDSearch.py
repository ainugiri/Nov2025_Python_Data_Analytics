import pandas as pd
df = pd.read_excel("NovTraining.xlsx")


print(df["Topic"].str.contains("AWS", case=False,na=False))
print(df[df["Topic"].str.contains("AWS", case=False,na=False)])


print(df.iloc[0:5])
print(df.iloc[[1,2,12,22,23,30]])

print("Trainer name: ",df.loc[0:20,"Trainer "])
print("df.head()",df.head())
print("df.tail()",df.tail())
print("df.info()",df.info())
print("df.shape",df.shape)
print("df.describe()",df.describe())
print("df.columns",df.columns)


print(df["Trainer "])

df["GST"] = df["Cost"] * 0.18
print("df.columns",df.columns)
print("df.describe()",df.describe())

df.columns = df.columns.str.strip()
print(df.head())

print(df["Trainer"])

df.rename(columns={"GST":"Tax"}, inplace=True)
print(df.head())
print("Welcome")
df.sort_values("Tax",ascending=False, inplace=True)
print(df)

print(df.groupby("Start Date")["Topic"].count())
print(df.groupby("Trainer")["Topic"].count())
print(df.groupby("Trainer")["Tax"].agg(["count","min","max","mean"]))
print(df.groupby("Start Date")["Tax"].agg(["count","min","max","mean"]))
print(df.groupby("Topic")["Tax"].agg(["count","min","max","mean"]))

df.drop_duplicates(inplace=True)
df.dropna(inplace = True)
df.fillna(0, inplace=True)

