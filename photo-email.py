from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
import smtplib

msg = MIMEMultipart()
msg.attach(MIMEText(file("text.txt").read()))
msg.attach(MIMEImage(file("image.png").read()))

# to send
mailer = smtplib.SMTP()
mailer.connect()
mailer.sendmail(from_, to, msg.as_string())
mailer.close()
