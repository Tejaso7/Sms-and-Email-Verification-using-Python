import os
import math
import random
import smtplib
from twilio.rest import Client

digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP + " is your One Time Password\nPlease Do not share with any one!"
msg= otp

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("tejusawant302@gmail.com", "sieirgniyexhyjeu")
emailid = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&',emailid,msg)

a = input("Enter Your OTP >>: ")
if a == OTP:
    print("Verified")

    digits = "0123456789"
    otp1=""
    for i in range(6):
      otp1+=digits[math.floor(random.random()*10)]
    account_sid = "ACa399677563aff5f0c0219d25bc63acdc"
    auth_token = '95916e3589f9f31451ff56f1d6f05ccd'
    client = Client(account_sid,auth_token)
    mobile = input("\nEnter Your Mobile Number (with Country code)>>: ")
    msg = client.messages.create(
        body ="\n\n" + otp1 + " is Your One Time Password \n Please Do not share with anyone",
        from_ = "+18482855490",
        to = mobile
        )
    b = input("Enter Your OTP >>: ")
    if b == otp1:
      print("Verified")
    else:
      print("Wrong OTP ! Try again")

else:
    print("Wrong OTP ! Try again")