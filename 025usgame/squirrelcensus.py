import pandas as pd

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# create a csv of squirrel count of fur color
fur_dict = {}
# print(df['Primary Fur Color'].unique())
for i in df['Primary Fur Color'].unique():
    # print(i)
    fur_dict[i] = df[df['Primary Fur Color'] == "Gray"].count()
# gray_fur = df[df['Primary Fur Color']=="Gray"].count()
# print(fur_dict["Black"])
print(fur_dict)