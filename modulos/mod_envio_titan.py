import smtplib
import imaplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.header import Header

#si jala falta solo agregar la firma con imagen 

# Email configuration
sender_email = 'correo que envia' 
sender_password = 'contra'
recipient_email = 'correo destinatario'
subject = 'Propuesta'
body = '''cuerpo'''

# Archivo adjunto
attachment_file = 'nombre del archivo falta agregar otro'

# SMTP (sending) server details
smtp_server = 'smtp.titan.email'
smtp_port = 587

# IMAP (receiving) server details
imap_server = 'imap.titan.email'
imap_port = 993

def send_email():
    # Create the message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = Header(subject, 'utf-8')

    # Agrega el cuerpo del correo electrónico
    message.attach(MIMEText(body, 'plain', 'utf-8'))

    # Agrega el archivo adjunto
    with open(attachment_file, 'rb') as f:
        attachment = MIMEBase('application', 'octet-stream')
        attachment.set_payload(f.read())
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', f'attachment; filename= {attachment_file}')
    message.attach(attachment)

    try:
        # Send the email
        smtp_obj = smtplib.SMTP(smtp_server, smtp_port)
        smtp_obj.starttls()
        smtp_obj.login(sender_email, sender_password)
        smtp_obj.sendmail(sender_email, recipient_email, message.as_string())
        smtp_obj.quit()
        print('Email sent successfully.')

        # Append the sent email to the IMAP server's "Sent" folder
        imap_obj = imaplib.IMAP4_SSL(imap_server, imap_port)
        imap_obj.login(sender_email, sender_password)
        imap_obj.append('Sent', '', imaplib.Time2Internaldate(imaplib.Time2Internaldate(imaplib.Time2Internaldate(time.time()))), message.as_bytes())
        imap_obj.logout()
        print('Email appended to "Sent" folder.')
    except smtplib.SMTPException as e:
        print('Error sending email:', str(e))
    except imaplib.IMAP4.error as e:
        print('Error appending email to "Sent" folder:', str(e))

# Call the function to send the email and append it to the "Sent" folder
send_email()