import pandas as pd

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# create a csv of squirrel count of fur color
fur_dict = {
    "Fur Color" : df['Primary Fur Color'].unique(),
    "Count" : []
}
# print(df['Primary Fur Color'].unique())
for i in fur_dict["Fur Color"]:
    fur_dict["Count"].append(len(df[df['Primary Fur Color']==i]))


fur_color_df = pd.DataFrame(fur_dict)
fur_color_df.to_csv("./squirrel_fur_count.csv")