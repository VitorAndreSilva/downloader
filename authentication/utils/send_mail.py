from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

def registration_request(user):
    admins = User.objects.filter(is_staff=True, is_active=True)
    emails = [admin.email for admin in admins if admin.email]

    send_mail(
        subject="Novo usuário aguardando aprovação",
        message=f"Novo cadastro: {user.email}",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=emails,
    )