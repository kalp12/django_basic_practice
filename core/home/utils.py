from django.core.mail import send_mail, EmailMessage
from django.conf import settings

def send_email_to_client():
    subject = 'Test sent from django'
    message = 'This is test message from django server'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['kalpmegh2000@gmail.com']
    send_mail(subject, message, from_email, recipient_list)

def send_email_to_client(file_path):
    subject = 'Test sent from django'
    body = 'This is test message from django server'
    from_email = settings.EMAIL_HOST_USER
    to = ['kalpmegh2000@gmail.com']
    mail = EmailMessage(subject, body, from_email, to)
    mail.attach_file(file_path)
    mail.send()
