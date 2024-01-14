from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings


def index(request):
    
    
    return render(request= request, template_name="index.html", context={})

def about_us(request):
    
    return render(request= request, template_name="about_us.html", context={})

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        category = request.POST.get('optradio', 'Other')
        print(name, email, message, category)
        # Customize the email content
        email_content = f"Name: {name}\nEmail: {email}\nMessage: {message}\nCategory: {category}"

        # Send the email using Django's send_mail function
        send_mail(
            'New Contact Form Submission',
            email_content,
            settings.DEFAULT_FROM_EMAIL,  # Replace with your default 'from' email
            ['syoyo1095@gmail.com'],  # Replace with your target email address
            fail_silently=False,
        )

        return HttpResponse('Email sent successfully')
    return render(request= request, template_name="contact_us.html", context={})