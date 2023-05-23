# readlines includes all of newline and strings
# with open("weather_data.csv","r") as data_file:
#     data = data_file.readlines()

# print(data)


# lot of work for just 1 row of data
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

#     print(temperatures)

import pandas as pd
data = pd.read_csv("weather_data.csv")
print(data)