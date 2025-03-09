from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.forms import ValidationError
from django.contrib.auth import login,logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from .forms import RegistrationForm,LoginForm 


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "accounts/login.html", {"form": form})

    def post(self, request):
        form = LoginForm(data=request.POST)  # ✅ Form bilan ishlash
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Welcome back!")  # ✅ Foydalanuvchiga hush kelibsiz deb aytish
            return redirect("home")

        # ✅ Form xatolarini avtomatik chiqarish
        messages.error(request, "Invalid username or password")
        return render(request, "accounts/login.html", {"form": form})

class RegisterView(View):
    form_class =RegistrationForm  # ✅ Formani klass o'zgaruvchisi sifatida belgilash
    template_name = "accounts/registrations.html"  # ✅ Shablonni klass o'zgaruvchisida belgilash

    def get(self, request):
        form = self.form_class()  
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        if request.method == "POST":
            form = RegistrationForm(request.POST)  
        if form.is_valid():
            user = form.save()  
            login(request, user)  
            messages.success(request, "Account created successfully!")  
            return redirect("home")  
        else:
            form = RegistrationForm()
        return render(request, self.template_name, {"form": form})
        
class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "You have been logged out.")  
        return redirect("home")