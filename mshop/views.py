from django.shortcuts import render
from datetime import datetime
from .models import Product
# Create your views here.


def index(request):
    now = datetime.now()
    products = Product.objects.all()
    return render(request, 'mshop.html', locals())
