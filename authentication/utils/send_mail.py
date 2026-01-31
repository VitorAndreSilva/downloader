import os
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.conf import settings
from config.settings import BASE_DIR

def registration_request(user):
    admins = User.objects.filter(is_staff=True, is_active=True)
    emails = [admin.email for admin in admins if admin.email]

    try:
        with open(os.path.join(BASE_DIR, "authentication/templates/email.html"), "r", encoding="utf-8") as file:
            html = file.read()
            html = html.replace("{{email}}", user.email)

        message = strip_tags(html)

        send_mail(
            subject="Novo usuário aguardando aprovação",
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=emails,
            html_message=html
        )

    except Exception as e:
        print("Falha ao enviar email: ", e)