from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, template_name='about.html')

def contact(request):
    return render(request, template_name='contact.html')

def gallery(request):
    return render(request, template_name='gallery.html')

def gallery_single(request):
    return render(request, template_name='gallery-single.html')

def index(request):
    return render(request, template_name='index.html')

def services(request):
    return render(request, template_name='services.html')

def starter_page(request):
    return render(request, template_name='starter-page.html')