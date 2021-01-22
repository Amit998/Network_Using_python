import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


server=smtplib.SMTP('smtp.world4you.com',25)

server.ehlo()


with open('password.txt','r') as pw:
    password=pw.read()

server.login('damitlucky998@gmail.com',password)


with open('password.txt','r') as m:
    message=m.read()

msg=MIMEMultipart()
msg['From']='AMIT'
msg['To']='damitlucky998gmail.com'
msg['Subject']='Just A Text'
msg.attach(MIMEText(message,'plain'))


filename='image.gif'

attachment=open(filename,'rb')


p=MIMEBase('application','octet-stream')
p.set_payload(attachment.read())


encoders.encode_base64(p)
p.add_header('Content-Disposition',f'attachedment; filename={filename}')



text=msg.as_string()
server.sendmail('damitlucky998@gmail.com','damitlucky998@gmail.com',text)