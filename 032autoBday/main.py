import smtplib
import datetime as dt
import pandas as pd
import random

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
df = pd.read_csv("birthdays.csv")
birthdays = df.to_dict(orient="list")
print(birthdays)



# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day

for i in range(len(birthdays["month"])):
    if birthdays["month"][i] == month and birthdays["day"][i] == day:
        print(f"It's {birthdays['name'][i]}'s birthday!")
        name = birthdays['name'][i]
        email = birthdays['email'][i]

        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        bday_file = f"./letter_templates/letter_{random.randint(1,3)}.txt"
        with open(bday_file) as file:
            # read -> string vs readlines -> list
            bday_text = file.read()
            # replace the template with name and join as a string
            bday_text = "".join([l.replace('[NAME]',name) for l in bday_text])
            



# 4. Send the letter generated in step 3 to that person's email address.
with smtplib.SMTP("smtp.gmail.com") as connection:
    # secure connection to email
        connection.login(user=gmail_email,gmail_password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject: Happy Birthday\n\n{bday_text}"
        )
        print(msg)
