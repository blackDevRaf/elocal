from unicodedata import name
from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name="home"),
    path("products/<str:pk>",views.product,name="product_detail"),
    #path("test/",views.order,name="test")

]