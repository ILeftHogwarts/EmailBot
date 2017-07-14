import smtplib 
from email.headerregistry import Address
from email.message import EmailMessage


message = EmailMessage()


with open('mail.html') as ml:
    mail_text = ml.read()
    message.set_content(mail_text, subtype = 'html')

message['From'] = 'teatrkolisei@gmail.com'
message['To'] = (Address('Andrew Dementiev', 'liken2134', 'gmail.com'))
message['Subject'] = 'Test mail'

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login("teatrkolisei@gmail.com", "ColiseumTheatre2017")
server.ehlo()
server.send_message(message)
server.quit()
print('Check mail box')