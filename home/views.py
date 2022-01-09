from django.shortcuts import render
from django.core.mail import send_mail
import environ

env = environ.Env()
environ.Env.read_env()

def index(request):

    if request.method == "POST":

        # Get values for the mail
        name = request.POST['input-name']
        mail = request.POST['input-mail']
        topic = request.POST['input-topic']
        message = request.POST['input-message']

        # Send e-mail
        send_mail(
            subject=f'{name} -> {topic}', 
            message=message,
            from_email=mail,
            recipient_list=[env("RECIPIENT_ADDRESS")]
        )
        
        # Return "thanks for contacting us" page
        return render(request, 'contact.html')

    else:
        return render(request, 'index.html', {})

def contact(request):
        return render(request, "contact.html", {})

def kids(request):
    return render(request, "kursy_dla_dzieci.html", {})

def teens(request):
    return render(request, "kursy_dla_nastolatkow.html", {})

def adults(request):
    return render(request, "kursy_dla_doroslych.html", {})

def events(request):
    return render(request, "wydarzenia.html", {})