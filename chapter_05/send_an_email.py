import smtplib

sender = 'sender@gmail.com' 
receiver = 'receiver@gmail.com'
password = 'fenton.RAV998'
subject = 'Python email test'
body = 'I wrote an email! :D'

message = f"""FROM: {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

try:
  server.login(sender, password)
  print('Logged in...')
  server.sendmail(sender, receiver, message)
  print('Email has been sent!')
except smtplib.SMTPAuthenticationError:
  print('unable to sign in')
except smtplib.SMTPServerDisconnected:
  print('connection error occured')
