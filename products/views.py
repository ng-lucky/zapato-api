from django.shortcuts import render
from .models import *
from .serializer import *
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from rest_framework import viewsets

# Create your views here.

def get_all_products(request):
    # get all products in db
    products = Product.objects.all() #Get all products
    return render(request, "products.html", {"enya_products": products} )

def get_a_product(request, product_id):
    product = None
    try:
        product = Product.objects.get(id=product_id)

    except Product.DoesNotExist:
        product = None
    
    return render(request, 'product.html', {"chechi_product": product})

def get_all_product_json(request):
    products = Product.objects.all()
    json_data = serializers.serialize("json", products)
    # print(json_data)
    return JsonResponse({"results": json_data})

class ProductsViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # def edit_product(self, request):
    #     return 

    