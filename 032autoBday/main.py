import smtplib
import datetime as dt

my_email = ""
password = ""

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     # secure connection to email
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="",
#         msg="Subject:Hello\n\nThis is the body of the email."
#         )

dt.datetime.now()