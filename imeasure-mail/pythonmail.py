import mysql.connector
import sys
import smtplib
from email.mime.text import MIMEText
import base64
import os
import delegator
import subprocess



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="noc@nextroll",
  database="Adroll"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT COUNT(id) FROM posts_post WHERE resolvedby='noc' OR status='pending'")

myresult = mycursor.fetchall()

for x in myresult:
    file=open("/home/itadmin/imeasure-tracker/imeasure-mail/output.txt", "w")
    file.close()
    str = x[0]
    #print(str)
    if str == 0:
        print ('nothing to display')
        pass
    else:
        mycursor.execute("SELECT id,shyft,dete FROM posts_post WHERE resolvedby='noc' OR status='pending'")
        newresult = mycursor.fetchall()
        length=len(newresult)
        for n in range(length):
            print(newresult[n][0],newresult[n][1],newresult[n][2], file=open("/home/itadmin/imeasure-tracker/imeasure-mail/output.txt", "a"))
            n = n+1
        subprocess.run(['bash', '/home/itadmin/imeasure-tracker/imeasure-mail/mysql.sh'])

os.remove("/home/itadmin/imeasure-tracker/imeasure-mail/output.txt")
