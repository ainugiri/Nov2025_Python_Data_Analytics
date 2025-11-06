import pandas as pd
df = pd.read_excel("NovTraining.xlsx")
# print(df.head(2))
# print(df["Topic"])

# print(df[df["Trainer "] == "Giri Prasad P"])
# print(df[(df["Trainer "] == "Jana") & (df["Topic"] == "Prompt Engineering Expert")])

print(df)

# df = df.drop("Trainer2 ",axis=1)
# print(df.head())

print(df[df["Cost"] >= 16500])
df.drop(df[df["Cost"] >= 16500].index, inplace=True)
print(df)

df.to_excel("NovTraining.xlsx", index=False)