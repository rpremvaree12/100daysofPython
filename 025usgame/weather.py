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
# two main types in pandas - dataframe and series
# data is a dataframe - table with columns and rows
# print(type(data))
temp_series = data["temp"]
# series - one column of values as a list
# print(temp_series)

# dictionary of values with column labels as keys and rows as values
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# find average temp
# total = 0
# for t in temp_list:
#     total += t
# print(f"The average temp is {round(total/len(temp_list),2)} C.")

# FASTER way to find average temp
# average_temp = round(sum(temp_list)/len(temp_list),2)
# print(f"The average temp is {average_temp} C.")

# EVEN FASTER using pandas method
# print(f"The average temp is {data['temp'].mean()} C.")

# data.condition or data['condition']

# get one row of data
# print(data[data.day == "Monday"])

# get row of data where the temp was the highest
# print(data[data.temp == data.temp.max()])

# get monday's temperature and convert to F
# mon_data = data[data.day == "Monday"]
# print(f"Monday's temp is {mon_data.temp * 9/5 + 32} F")

# create a data frame from scratch
data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
}
data = pd.DataFrame(data_dict)
print(data)
data.to_csv("./new_weather_data.csv")