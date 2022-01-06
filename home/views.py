from django.shortcuts import render
from django.core.mail import send_mail
import time

# Create your views here.

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
            recipient_list=['marcin26012000@gmail.com']
        )
        
        # Return "thanks for contacting us" page
        return render(request, 'contact.html')

    else:
        return render(request, 'index.html', {})

def contact(request):
    return render(request, "contact.html", {})
