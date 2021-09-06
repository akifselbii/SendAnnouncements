#Mehmet Akif Selbi

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import String as st

def Mail(subject,body,mail): 
    msg = MIMEMultipart()

    msg['From'] = st.comuAnnouncement
    msg['To'] = str(mail)
    msg['Subject'] = str(subject)

    body = str(body)
    body_text = MIMEText(body, "plain")
    msg.attach(body_text)
     
    server = smtplib.SMTP('smtp.gmail.com: 587')
     
    server.starttls()
     
    server.login(st.baseMail, st.password)#email and password
     
     
    server.sendmail(msg['From'], msg['To'], msg.as_string())
     
    server.quit()
     
    print (st.successfulSending % (msg['To']))
