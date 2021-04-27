from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('about', views.about, name='aboutpage'),
    path('portfolio', views.portfolio, name='portfoliopage'),
    path('services', views.services, name='servicespage'),
]

