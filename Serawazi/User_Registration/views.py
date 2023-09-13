from django.shortcuts import render

# from .authentication import EmailAuthBackend
# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

def sender_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/sendgig')
        else:
            messages.error(request, 'Invalid credentials!')
            return redirect('user:sender-login')
    
    return render(request, 'user/sender-login.html')
