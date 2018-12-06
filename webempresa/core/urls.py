from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('services/', views.services),
    path('store/', views.store),
    path('contact/', views.contact),
    path('blog/', views.blog),
    path('sample/', views.sample)
    ]