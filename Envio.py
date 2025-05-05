import os
import smtplib
from email.message import EmailMessage
from Senha import senha 


#configuração do email e senha

Email_Adress = 'SEU EMAIL'
Email_Password = senha

#criação de email

msg = EmailMessage()
msg['Subject'] = 'ASSUNTO'
msg[ 'From' ] = Email_Adress
msg['To'] = 'EMAIL DO DESTINATARIO'
msg.set_content('MENSAGEM EXEMPLO')

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(Email_Adress, Email_Password)
    smtp.send_message(msg)

