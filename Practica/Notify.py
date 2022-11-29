import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

COMMASPACE = ', '
# Define params
imgpath = '/home/user/Documentos/Administracion-Servicios-Red/Ejercicio-Umbral/'

mailsender = "danbobadilla8@gmail.com"
mailreceip = "danbobadilla8@gmail.com"
mailserver = 'smtp.gmail.com: 587'
password = 'kyfpxnhlfrcirdtv'

def send_alert_attached(subject):
    """ Envía un correo electrónico adjuntando la imagen en IMG
    """
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = mailsender
    msg['To'] = mailreceip
    mensaje = MIMEText(subject,"plain")
    msg.attach(mensaje)
    s = smtplib.SMTP(mailserver)

    s.starttls()
    # Login Credentials for sending the mail
    s.login(mailsender, password)

    s.sendmail(mailsender, mailreceip, msg.as_string())
    s.quit()