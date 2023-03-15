# #automated birthday wisher

import smtplib
import datetime as dt
import random
import os

#open quote file
with open(file="../quotes.txt") as f:
    quotes=f.readlines()
#Pick Random Quote
motivateQuote=random.choice(quotes)
receiver_email=os.environ.get("RECEIVER_EMAIL")
sender_email= os.environ.get("SENDER_EMAIL")
my_password=os.environ.get("PASSWORD")
#-------------Connection Establishment------------
#Smtp-->Simple Mail Transfer Protocol
now=dt.datetime.now()

if now.weekday()==0:
    with smtplib.SMTP("smtp.gmail.com",587,timeout=120) as connection :
    #     #secure connection
        connection.starttls()
        connection.login(user=sender_email, password=my_password)
        connection.sendmail(from_addr=sender_email, to_addrs=receiver_email, msg=f"subject:Monday Motivitional Quote\n\n{motivateQuote}")
























# #-------------Sender Email and Password----------
# my_email="gameelgamal001@gmail.com"
# my_password="xepzmhfrcrcwettq"
# #-------------Connection Establishment------------
# #Smtp-->Simple Mail Transfer Protocol 
# with smtplib.SMTP("smtp.gmail.com",587,timeout=120) as connection :
#     #Secure Connection
#     connection.starttls()
#     connection.login(user=my_email,password=my_password)
#     connection.sendmail(from_addr=my_email,to_addrs="houssein_habib.1995@hotmail.com",msg=f"Subject:Hello\n\nHello With a Subject")


# now=dt.datetime.now()
# print(now)


