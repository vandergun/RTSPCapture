import rtsp
import PyQt5
from rtsp import Client
import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import time
from datetime import datetime

#RTSP Function

client = rtsp.Client(rtsp_server_uri = 'rtsp://<username>:<password>@<IP address of device>:<RTSP port>/Streaming/channels/<channel') # eg: rtsp://Hikvision:guest@192.168.1.168:10554/Streaming/channels/1701 , This mean get the main stream of the 17th channel (1st IP camera on the Hybrid Demo)
client.read().save(fp="E:\camera1.png")
client = rtsp.Client(rtsp_server_uri = 'rtsp://<username>:<password>@<IP address of device>:<RTSP port>/Streaming/channels/<channel')
client.read().save(fp="E:\camera2.png")
client = rtsp.Client(rtsp_server_uri = 'rtsp://<username>:<password>@<IP address of device>:<RTSP port>/Streaming/channels/<channel')
client.read().save(fp="E:\camera3.png")
client = rtsp.Client(rtsp_server_uri = 'rtsp://<username>:<password>@<IP address of device>:<RTSP port>/Streaming/channels/<channel')
client.read().save(fp="E:\camera4.png")
client.close()

time.sleep(5)

# MAILING FUNCTION
smtp_server = "smtp.office365.com"
smtp_port = 587  # for smtp.gmail.com
from_address = "sender@example.com"  # e.g. username@gmail.com ; Email of sender
sender_name = "Sender name of email " # This is Sender Name
from_password = "P@ssw0rd"  # required by script to login using your username
to_address = "receiver@example.com"  # e.g. username2@gmail.com
subject = "DNC" # Title of email
mail_body = str(datetime.now())
attachment_1 = r"E:\camera1.png"  # e.g. file = r"C:\Folder1\text1.txt" # if you attach more than two files here, be sure to append them to the files dictionary below, as done for attachemnt_1 and attachment_2.
attachment_2 = r"E:\camera2.png"
attachment_3 = r"E:\camera3.png"
attachment_4 = r"E:\camera4.png"
msg = MIMEMultipart()
msg['Subject'] = subject
msg['From'] = sender_name
msg['To'] = to_address
msg.attach(MIMEText(mail_body))
files = []
files.append(attachment_1)
files.append(attachment_2)
files.append(attachment_3)
files.append(attachment_4)
for file in files:
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(file, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(os.path.basename(file)))
    msg.attach(part)
server = smtplib.SMTP(smtp_server, smtp_port)
server.ehlo()
server.starttls()
server.login(from_address, from_password)
server.sendmail(from_address, to_address, msg.as_string())
server.quit()
##


