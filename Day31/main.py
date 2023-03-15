#automated birthday wisher

import smtplib

#-------------Sender Email and Password----------
my_email="gameelgamal001@gmail.com"
my_password="xepzmhfrcrcwettq"
#-------------Connection Establishment------------
#Smtp-->Simple Mail Transfer Protocol 
with smtplib.SMTP("smtp.gmail.com",587,timeout=120) as connection :
    #Secure Connection
    connection.starttls()
    connection.login(user=my_email,password=my_password)
    connection.sendmail(from_addr=my_email,to_addrs="houssein_habib.1995@hotmail.com",msg=f"Subject:Hello\n\nHello With a Subject")

