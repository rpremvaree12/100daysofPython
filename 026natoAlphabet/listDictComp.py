import random
import pandas as pd
# keyword method
# new_list = [new_item for item in list]

# old way
numbers = [1,2,3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
# new_list.append(add_1)

# list comprehension
new_list = [n + 1 for n in numbers]
print(f"Numbers + 1: {new_list}")

# Python sequences - list, range, string, tuple
doubles = [n*2 for n in range(1,5)]
print(f"Doubled numbers: {doubles}")

# conditional list comprehension
# new_list = [new_item for item in list if test]
names = ["Alex","Beth","Caroline","Eleanor","Freddie"]
short_names = [name for name in names if len(name) < 5]
print(f"Short names: {short_names}")
long_names = [name.upper() for name in names if len(name) > 5]
print(f"Long names: {long_names}")


# find data overlap

with open("file1.txt") as f1:
    f1_numbers = f1.readlines()
    f1_clean = [int(i) for i in f1_numbers]

with open("file2.txt") as f2:
    f2_numbers = f2.readlines()
    f2_clean = [int(i) for i in f2_numbers]

# Write your code above 👆
result = [n for n in f1_clean if n in f2_clean]
print(result)


# Dictionary comprehension
# new_dict = {new_key:new_item for item in list}
# new_dict = {new_key:new_item for (key,value) in dict.items()}
# new_dict = {new_key:new_item for (key,value) in dict.items() if test}
names = ["Alex","Beth","Caroline","Eleanor","Freddie"]
student_scores = {name:random.randint(0,100) for name in names}
print(student_scores)

passed_students = {name:score for (name,score) in student_scores.items() if score >= 60}
print(passed_students)

# dictionary comp - find number of characters in a sentence
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}
print(result)

# dictionary comp - cover c to f
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day:temp*9/5 + 32 for (day,temp) in weather_c.items()}
print(weather_f)


# iterating over dataframe using iterrows
student_data = {
    "students" : ["Angela", "James", "Lily"],
    "scores" : [56, 76, 98]
}
student_df = pd.DataFrame(student_data)
for (index, row) in student_df.iterrows():
    # get hold of each student
    print(row.student)
    print(row.score)
