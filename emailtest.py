import smtplib

smtp_object = smtplib.SMTP('smtp.gmail.com',587)
smtp_object.ehlo()
smtp_object.starttls()
password= input("Password please: ")
email=input("Email:")
print(smtp_object.login(email,password))
from_address=email
to_address=email
subject=input("Enter the subject line: ")
message=input("Enter the body message: ")
msg="Subject: "+subject+'\n'+message

smtp_object.sendmail(from_address,to_address,msg)
print(smtp_object.quit())
'''
   Password please: fqumcvcrycchqqob
Email:simminagdeo@gmail.com
(235, b'2.7.0 Accepted')
Enter the subject line: python mail
Enter the body message: yes generated
(221, b'2.0.0 closing connection w63sm18555309pfc.20 - gsmtp')
'''