from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render


def index(request):
    if request.method == "POST":
        patient = request.POST["patient"]
        doctor = request.POST["doctor"]
        department = request.POST["department"]
        email = request.POST["email"]
        symptoms = request.POST["symptoms"]
        date = request.POST["date"]

        subject = "Medical website - Message received."
        message = f"Dear {patient}\nwe have received your message and will get back to you soon!"
        sender = settings.EMAIL_HOST_USER
        recipients = [email]
        send_mail(subject, message, sender, recipients)

        return render(request, 'index.html', {"patient": patient})

    else:
        return render(request, 'index.html', {})
