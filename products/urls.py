from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()

router.register("products_api", ProductsViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('get_all', get_all_products),
    path('<int:product_id>/', get_a_product),
    path('json_products/', get_all_product_json)
]