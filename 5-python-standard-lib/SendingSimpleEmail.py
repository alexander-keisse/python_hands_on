from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from pathlib import Path

message = MIMEMultipart()
message['from'] = "Mr Robot"
message['to'] = "Society"
message['subject'] = "Wisdom"
message.attach(MIMEText(Path('../exceptions/txt-files/second_file.txt').read_text()))

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('faker@gmail.com', 'alwaysuseapasswordsentenceWithUppercaseAndNumbersOrSymols5?!')
    print('Sent...')
