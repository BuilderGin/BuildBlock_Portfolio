from django.urls import path

from . import views

urlpatterns = [
    # path('contactpage/', views.index, name='contactpage'),
    path('', views.contact, name='contact'),
]