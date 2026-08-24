#refered data.csv file
import pandas as pd

df = pd.read_csv("data.csv")
tall_pokemon = df[df["Height"]>=2]
heavy_pokemon=df[df["Weight"]>100]
print(heavy_pokemon)
print(tall_pokemon)
legendary_pokemon=df[df["Legendary"]==True]
print(legendary_pokemon)
water_pokemon=df[(df["Type1"]=="Water")|(df["Type2"]=="Water")]
print(water_pokemon)
ff_pokemon=df[(df["Type1"]=="Fire")|(df["Type2"]=="Flying")]
print(ff_pokemon)
