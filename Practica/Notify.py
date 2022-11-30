import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

COMMASPACE = ', '
# Define params
rrdpath = '/home/user/Documentos/Administracion-Servicios-Red/Ejercicio-Umbral/'
imgpath = './'
fname = 'trend.rrd'

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
    fp = open(imgpath+'deteccion.png', 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    msg.attach(img)
    s = smtplib.SMTP(mailserver)

    s.starttls()
    # Login Credentials for sending the mail
    s.login(mailsender, password)

    s.sendmail(mailsender, mailreceip, msg.as_string())
    s.quit()