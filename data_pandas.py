# panda - handline
# series / dataframe
# onedim / two
#  pip install pandas
import pandas as pd
s1 = pd.Series([11,12,14,18,21])
print(s1)

score = {
    "overs" : [1,2,3,4,5,6,7,8,9],
    "TeamA" : [12,20,28,34,40,49,52,60,72],
    "TeamB" : [8,10,38,43,47,49,52,60,73]
}

print(score)

df = pd.DataFrame(score)
print(df)

df = pd.read_csv("./customers-100.csv")
print(df)
print(df.head(25))

# df = pd.read_excel("./Book1.xlsx")
print(df)


score = {
    "overs" : [1,2,3,4,5,6,7,8,9],
    "TeamA" : [12,20,28,34,40,49,52,60,72],
    "TeamB" : [8,10,38,43,47,49,52,60,73]
}

print(score)

df = pd.DataFrame(score)

# df.to_csv("./score.csv", index=False)

df = pd.read_excel("NovTraining.xlsx", sheet_name="Sheet1")
print(df.head())