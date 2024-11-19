import smtplib
import datetime as dt
import pandas as pd
import random

##################### Extra Hard Starting Project ######################

# format today's date as a tuple
today = (dt.datetime.now().month, dt.datetime.now().day)

# format birthdays as a dictionary with tuples (bday_month, bday_day): data_row
df = pd.read_csv("birthdays.csv")

# dict comp for df
birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in df.iterrows()}

if today in birthdays_dict:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        bday_file = f"./letter_templates/letter_{random.randint(1,3)}.txt"
        bday_person = birthdays_dict[today]
        with open(bday_file) as file:
            bday_text = file.read()
            # replace the template with name and join as a string
            bday_text = "".join([l.replace('[NAME]',bday_person['name']) for l in bday_text])
            print(bday_text)



# 4. Send the letter generated in step 3 to that person's email address.
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     # secure connection to email
#         connection.login(user=gmail_email,gmail_password=password)
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs=email,
#             msg=f"Subject: Happy Birthday\n\n{bday_text}"
#         )

