# Sending mail using gmail smtp server

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
smtp_server = 'smtp.gmail.com'
# Email configuration for Outlook
# smtp_server = 'smtp.office365.com'
smtp_port = 587
username = 'antilparul@gmail.com'
password = 'wlix nmym sybi anzc'

# Create the email content
subject = 'Subject of the Email'
body = 'This is the body of the email.'

msg = MIMEMultipart()
msg['From'] = username
msg['To'] = 'example@gmail.com'
msg['Subject'] = subject

# Attach the email body
msg.attach(MIMEText(body, 'plain'))

# Connect to the SMTP server and send the email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Secure the connection with TLS
    server.login(username, password)
    server.send_message(msg)
    print('Email sent successfully!')

except Exception as e:
    print(f'Failed to send email: {e}')

finally:
    server.quit()
