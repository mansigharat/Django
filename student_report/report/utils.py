from report.models import *
import time
from student_report import *
from django.core.mail import send_mail
from django.conf import settings

def send_email_to_client():
    subject = "This email from django server"
    message = "Hello my future SDE"
    from_email = settings.EMAIL_HOST_USER
    recipent_list = ['mansigharat1909@gmail.com']

    send_mail(subject, message, from_email, recipent_list)

