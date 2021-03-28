import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Gmail:
  def __init__(self, recipient, subject, message):
    self.recipient = recipient
    self.subject = subject
    self.message = message

  def send(self):
    

    email = "sdasds@gmail.com" # your email
    password = "asdasda"
    recipient = self.recipient # to whom
    subject = self.subject
    message = self.message

    msg = MIMEMultipart()
    msg["From"] = email
    msg["To"] = recipient
    msg["Subject"] = subject

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, recipient, text)
    print('Email sent!!')
    server.quit()

# email = Gmail('ling.duke@gmail.com', 'Subject', 'Message')
# email.send()