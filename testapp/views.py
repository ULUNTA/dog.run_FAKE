from django.shortcuts import render
from django.http.response import HttpResponse

def index_template(request):
    return render(request, 'index.html')

def contact_template(request):
    return render(request, 'contact.html')

def about_template(request):
    return render(request, 'about.html')

def blog_template(request):
    return render(request, 'blog.html')

def portfolio_template(request):
    return render(request, 'portfolio.html')

def services_template(request):
    return render(request, 'services.html')

