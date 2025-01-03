import smtplib
import imaplib
import time
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.header import Header


#leer datos de quien envia
with open("datos.txt","r") as f:
    lineas = f.read().split(",")
    
#correos a enviar ese correo
with open("correos.txt","r") as f:
    destinatarios = f.read().split(",")

# Email configuration
sender_email = lineas[0]#'correo que envia' 
sender_password = lineas[1] #'contra'
subject = 'PROPUESTA OLWAN S.C. SERVICIOS LEGALES'
copiao_email = 'contacto@olwan.com.mx' #copia oculta preferentemente olwan it o contacto
copiao_email2 = 'olwan_it@outlook.com'


# SMTP (sending) server details
smtp_server = 'smtp.titan.email'
smtp_port = 587

# IMAP (receiving) server details
imap_server = 'imap.titan.email'
imap_port = 993


# Agrega los archivo adjuntos
def add_attachment(message, file_path):
    with open(file_path, 'rb') as f:
        attachment = MIMEBase('application', 'octet-stream')
        attachment.set_payload(f.read())
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', f'attachment; filename= {os.path.basename(file_path)}')
    message.attach(attachment)
    
    
def send_email():
    # Create the message
    message = MIMEMultipart('alternative')
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = Header(subject, 'utf-8')

    # Agrega el cuerpo del correo electrónico y la firma como una sola parte de texto HTML
    html_body = f'''
        <html>
            <body>
            <p>Buen día, somos OLWAN S.C., despacho de abogados especialistas en el área de transportes, 
            misión es brindarle soluciones prácticas ante los problemas legales que suscite usted o su negocio,
            velando siempre por sus intereses, además de brindarle también asesoría en diversas ramas del derecho (fiscal, civil, penal, mercantil);
            nuestros clientes siempre tienen entera satisfacción de nuestros servicios, entre los cuales destacan: </p>
                <ul>
                <li> Trámites ante SICT (antes SCT), SEMARNAT, PROFEPA. </li>
                <li> Obtención de permisos para circular en diversos Estados de la República Mexicana. </li>
                <li> Liberaciones de unidades, atención de siniestros. </li>
                <li> Cobro de daños ante aseguradora, CONDUSEF. </li>
                <li> Impugnación de multas federales. </li>
                <li> Verificación de humos y físico mecánicas. </li>
                </ul>
            <p>¿Cómo contactarnos? </p>
            <p>Si necesita ayuda con un problema legal, no dude en contactarnos. Puede hacerlo a través de: </p>
            <p>Correo electrónico: Olwan.2024@hotmail.com contacto@olwan.com.mx sergiovalenzuela@olwan.com.mx jaimeluna@olwan.com.mx 
            jmartinez@olwan.com.mx guadalupevalenzuela@olwan.com.mx</p>
            <p>Tel- mensajería: 8141475841/ 8186581403</p>
            <p>OLWAN S.C., estará encantado de ayudarlo a resolver sus problemas legales de manera eficiente. </p>
            
            <br>
                <table border="0" cellpadding="5" cellspacing="5">
                    <tr>
                        <td>
                            <img src="https://olwan.com.mx/img/version1.png" alt="Firma" width="270px" height="220px">
                        </td>
                        <td valign="top">
                            <p><b>Jacob Rodriguez</b></p>
                            <p><b>Téfono:</b> 8132416879</p>
                            <p><b>Email:</b> jacob_rodriguez@olwan.com.mx</p>
                            <p>OLWAN S.C.</p>
                            <p>SERVICIOS JURIDICOS</p>
                            <p>SU TRANQUILIDAD NUESTRA PRIORIDAD</p>
                        </td>
                    </tr>
                </table>
            </body>
        </html>
    '''
    html_part = MIMEText(html_body, 'html', 'utf-8')
    message.attach(html_part)

    # Agrega los archivos adjuntos
    add_attachment(message, 'OLWAN S.C. FINAL SERVICIOS JURIDICOS.pdf')
    add_attachment(message, 'Propuesta_Olwan_v1.2.pdf')
    try:
        # Send the email
        smtp_obj = smtplib.SMTP(smtp_server, smtp_port)
        smtp_obj.starttls()
        smtp_obj.login(sender_email, sender_password)
        smtp_obj.sendmail(sender_email, [recipient_email, ' ', copiao_email, ' ' ,copiao_email2], message.as_string())
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


for destinatario in destinatarios:
    recipient_email = destinatario#correo destinatario
    # Call the function to send the email and append it to the "Sent" folder
    send_email()
    print(f"enviado a {destinatario}")
    if os.path.exists("correos_enviados_5agosto2.txt"):
        with open("correos_enviados_5agosto2.txt", "a") as archivo:
            archivo.write(f"enviado a {destinatario}")
    else:
        with open("correos_enviados_5agosto2.txt", "w") as archivo:
            archivo.write(f"enviado a {destinatario}")
    time.sleep(60)