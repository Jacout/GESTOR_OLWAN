import smtplib
import imaplib
import time
from email.mime.text import MIMEText
from email.header import Header

# Email configuration
sender_email = 'cuenta correo' 
sender_password = 'contraseña'
recipient_email = 'destinatario'
subject = 'Testing email script'
body = 'This is a test email sent from a Python script, saludos.'

# SMTP (sending) server details
smtp_server = 'smtp.titan.email'
smtp_port = 587

# IMAP (receiving) server details
imap_server = 'imap.titan.email'
imap_port = 993

def send_email():
    # Create the message
    message = MIMEText(body, 'plain', 'utf-8')
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = Header(subject, 'utf-8')

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