from django.shortcuts import render

def index(request):
    return render(request, 'galeria/index.html')


def image(request):
    return render(request, 'galeria/image.html')