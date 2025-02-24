from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
# Create your views here.

class CustomLoginForm(AuthenticationForm):
    pass
class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', context = {"form":form})
    
    def post(self, request):
         if request.method == "POST":
            username = request.POST.get("username", "").strip()
            password = request.POST.get("password", "").strip()
        
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")  # Redirect to home or another page
        
            else:
                 messages.error(request, "Invalid username or password.")
                
         return render(request, "accounts/login.html") 

class RegisterView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'accounts/regestrations.html',context={"form"})
    
    def post(self, request):
        pass