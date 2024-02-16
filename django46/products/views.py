from django.shortcuts import render

from .models import Category, ProductModel


def home_page(request):
    category_info = Category.objects.all()
    products_info = ProductModel.objects.all()
    context = {'categories': category_info, 'products': products_info}
    return render(request, 'index.html', context)
