from django.urls import path
from galeria.views import index
from galeria.views import image

urlpatterns = [
    path('', index, name='index'),
    path('image/', image, name='image'),
]