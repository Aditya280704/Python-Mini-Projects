import smtplib

my_email = "aj8364524@gmail.com"
password = "bhux ioiu gpaq xgvl"
receiver = "anishajoshi5210@gmail.com"

# Establishing connection with recipient mail
connection = smtplib.SMTP("smtp.gmail.com")
# Securing our connection to our email server(tls-transport layer security)
connection.starttls()
# Login into our email id
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email,
                    to_addrs=receiver,msg="Subject:Hello\n\nThis is body of my email")
connection.close()






