import smtplib
import datetime as dt
import random

now = dt.datetime.now()
year = now.year
month = now.month
day_week = now.weekday()

# read lines of the text file as a list
with open("quotes.txt") as file:
    quotes = file.readlines()

# sender email
gmail_email = "pythontest618@gmail.com"
gmail_password = "enmfhxnqomczzezj"

# choose a random quote and send email on Monday
if day_week == 0:
    quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
    # secure connection to email
        connection.starttls()
        connection.login(user=gmail_email,gmail_password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="",
            msg=f"Subject: Monday Motivation\n\n{quote}"
            )
        print(f"{quote} was sent to {gmail_email}")
        
date_of_birth = dt.datetime(year=1980, month=12, day=23)