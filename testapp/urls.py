from django.conf.urls import url
from . import views
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('', views.index_template, name='index'),
    path('contact/', views.contact_template, name='contact'),
    path('about/', views.about_template, name='about'),
    path('blog/', views.blog_template, name='blog'),
    path('portfolio/', views.portfolio_template, name='portfolio'),
    path('services/', views.services_template, name='services'),
    
]