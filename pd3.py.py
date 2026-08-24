#data cleaning
import pandas as pd
df = pd.read_csv("data.csv")
# df=df.drop(columns=["Legendary","No"])
# print(df)
df=df.fillna({"Type2":"None"})
print(df)

df["Type1"]=df["Type1"].replace({"Grass":"GRASS",
                                 "Fire": "FIRE",
                                 "Water": "WATER"})
print(df)
df["Legendary"]=df["Legendary"].astype(bool)
print(df["Legendary"])
