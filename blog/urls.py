from django.urls import path
from.views import index,about,client,contact,product
urlpatterns = [
    path('index/',index,name="index"),
    path('about/',about,name="about"),
    path('client/',client,name="client"),
    path('contact/',contact,name="contact"),
    path('product/',product,name="products")
]


