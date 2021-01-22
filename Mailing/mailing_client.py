import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
 

server = smtplib.SMTP('smtp.gmail.com',465)

server.ehlo()

# server.login('damitlucky998@gmail.com','password1234')

with open('password.txt','r') as f:
    password = f.read()


server.login('damitlucky998@gmail.com',password)

msg = MIMEMultipart()
msg['From']='AMIT DUTTA'
msg['To'] ='testmail@spaml.de'
msg['Subject'] =' Just A Test'

with open('msg.txt','r') as f:
    message = f.read()
msg.attach(MIMEText(message,'plain'))

filename='default-avatar.png'
attachment=open(filename,'rb')

p=MIMEBase('application','octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)

p.add_header('Content-Disposition',"f attachment; filename={filename}")
msg.attach(p)

text = msg.as_string()
server.sendmail('damitlucky998@gmail.com','testmails@spaml.de',text)