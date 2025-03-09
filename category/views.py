from django.shortcuts import render
from django.views import View
from .models import Category

# Create your views here.
class CategoryListView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, "category/category_list.html", {"categories": categories})