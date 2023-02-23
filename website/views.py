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

        return render(request, 'index.html', {"patient": patient})

    else:
        return render(request, 'index.html', {})
