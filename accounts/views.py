from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.forms import ValidationError
from django.contrib.auth import login,get_user_model
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

# ✅ Maxsus login form yaratish
class CustomLoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValidationError("This account is inactive.", code="inactive")

class LoginView(View):
    def get(self, request):
        form = CustomLoginForm()
        return render(request, "accounts/login.html", {"form": form})

    def post(self, request):
        form = CustomLoginForm(data=request.POST)  # ✅ Form bilan ishlash
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Welcome back!")  # ✅ Foydalanuvchiga hush kelibsiz deb aytish
            return redirect("home")

        # ✅ Form xatolarini avtomatik chiqarish
        messages.error(request, "Invalid username or password")
        return render(request, "accounts/login.html", {"form": form})

# class RegisterView(View):
#     form_class = UserCreationForm  # ✅ Formani klass o'zgaruvchisi sifatida belgilash
#     template_name = "accounts/registrations.html"  # ✅ Shablonni klass o'zgaruvchisida belgilash

#     def dispatch(self, request, *args, **kwargs):
#         if request.user.is_authenticated:  # ✅ Agar foydalanuvchi allaqachon login qilgan bo‘lsa
#             return redirect("home")  
#         return super().dispatch(request, *args, **kwargs)

#     def get(self, request):
#         form = self.form_class()  
#         return render(request, self.template_name, {"form": form})

#     def post(self, request):
#         form = self.form_class(request.POST)  
#         if form.is_valid():
#             user = form.save()  
#             login(request, user)  
#             messages.success(request, "Account created successfully!")  
#             return redirect("home")  
        
#         for field, errors in form.errors.items():
#             for error in errors:
#                 messages.error(request, f"{field.capitalize()}: {error}")  # ✅ Form xatolarini chiqarish
        
#         return render(request, self.template_name, {"form": form})
User = get_user_model()
class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "accounts/registrations.html", {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # ✅ Foydalanuvchini yaratish, lekin saqlamaslik
            user.save()  # ✅ Saqlash
            login(request, user)  # ✅ Avtomatik login qilish
            messages.success(request, "Account created successfully!")
            return redirect("home")  # ✅ Bosh sahifaga yo‘naltirish

        messages.error(request, "Registration failed. Please check the form.")
        return render(request, "accounts/registrations.html", {"form": form})