import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login('damitlucky998@gmail.com', 'Your Password')
server.sendmail(
  "damitlucky998@gmail.com", 
  "testmails@spaml.de", 
  "this message is from python")
server.quit()