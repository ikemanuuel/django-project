from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

User = get_user_model()


def activate_account(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()

        activation_link = f"{settings.BASE_URL}/activation/{uidb64}/{token}/"

        subject = 'Your account has been activated!'
        message = f'Your account has been activated. Thank you for using our application. You can now log in.'
        from_email = settings.EMAIL_HOST_USER
        to_email = user.email

        send_mail(subject, message, from_email, [to_email])
        messages.success(request, 'Your account has been activated.')
        return redirect('http://192.168.1.120:3000/Activated')
    else:
        messages.error(request, 'Activation link is invalid or has expired.')
        return redirect('http://localhost:3000/')
