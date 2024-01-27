from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import * 




def login_view(request):
    # create_user()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')  # Replace 'home' with the name of your home view
        else:
            # Authentication failed
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')