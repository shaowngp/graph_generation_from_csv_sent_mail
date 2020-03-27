#!/usr/bin/env python
# coding: utf-8
#Author: Imam Uddin Ahamed


# Sending mails to multiple recipients with attachment from Google Account which can be replaced by your organization / other smtp config. 

  
# Required libraries to import 
import smtplib 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email.mime.multipart import MIMEMultipart 
from email import encoders 

# Creating function/method to send mails with attachment 
def send_mail():
    # Mail sending from 
    sender = "xyz@gmail.com"

    # Mail recipients 
    receiver = [ "xyz@outlook.com","abc@gmail.com "] 

    # Mail cc recipients
    ccaddr = ["mnp@outlook.com"]

    # Message in MIMEMultipart 
    msg = MIMEMultipart() 

    # storing the senders email address   
    msg['From'] = sender 

    # storing the recipients email address  
    msg['To'] = ", ".join(receiver)

    msg['Cc'] = ", ".join(ccaddr)

    receiver.extend(ccaddr)

    # storing the subject  
    msg['Subject'] = "Test: Daily Average TPS"

    # string to store the body of the mail 
    body = "Hi, This is Test."

    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 

    # Storing file name in a variable to be sent  
    filename = "daily_avg_tps_03272020.png"
    
    # Opening required attachment file to be sent  
    attachment = open("D:\\Python_test\\daily_avg_tps_03272020.png", "rb") 

    # Instance of MIMEBase and named as appmime 
    appmime = MIMEBase('application', 'octet-stream') 

    # Changing the payload into encoded form 
    appmime.set_payload((attachment).read()) 

    # Encoding into base64 
    encoders.encode_base64(appmime) 

    appmime.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

    # Attaching the instance 'appmime' to instance 'msg' 
    msg.attach(appmime) 

    # Creating Google's SMTP session - for TLS : 587 , for ssl : 465 
    s = smtplib.SMTP('smtp.gmail.com', 587) 

    # Starting TLS for security 
    s.starttls() 

    print("Before Login to my mail account");  

    # Logging in using my email credentials

    s.login(sender, "XXXXXXX")  #--> Here "XXXXXX" represent your password. You can make it as property base.

    print("After Login to my mail account");  

    # Converts the Multipart msg into a string 
    text = msg.as_string() 

    
    # Sending the mail with attachment
    # Important: Beforesending mails, you have to enable "Allow less secure apps: ON" in your google account.
    # Ref. to enable "Allow less secure apps": https://myaccount.google.com/u/1/lesssecureapps?pageId=none

    s.sendmail(sender,receiver,text) 


    # Closing the session 
    s.quit() 


send_mail()

# For any queries & help, please let me know. mail id: shaowngp@outlook.com.
# I have taken helps from Various group & made customized as per my requirement. Hope it'll benefit you as well. :-)

