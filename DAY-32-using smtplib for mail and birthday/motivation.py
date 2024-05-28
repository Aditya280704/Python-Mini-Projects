import smtplib
import datetime as dt
import random

MY_EMAIL = "aj8364524@gmail.com"
MY_PASS = "bhux ioiu gpaq xgvl"
RECEIVER_EMAIL = "anishajoshi5210@gmail.com"

# Imported datetime class from datetime module which is initialized as dt
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 6:  # 0=monday,1=tuesday
    with open("quotes.txt") as quote_file:
        # read all line
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASS)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs=RECEIVER_EMAIL,
                        msg=f"Subject:Sunday Motivation\n\n{quote}")
    connection.close()




