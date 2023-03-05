from django.shortcuts import render
from .models import *
from .serializer import *
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import action
from django.core import serializers
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.permissions import AllowAny, IsAuthenticated

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

    @action(methods=['post'], detail=False, permission_classes = [AllowAny])
    def search_product(self, request):
        search_text = request.data.get("search_query", "")
        queryset = Product.objects.all()

        if search_text != "":
            queryset = queryset.filter(Q(name__contains=search_text) | \
                                        Q(description__contains=search_text))
        
        serializer = ProductSerializer(queryset, many=True)

        return Response({"results": serializer.data})



    # def edit_product(self, request):
    #     return 

    