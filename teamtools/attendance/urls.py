from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('scan/', views.scan, name='scan'),
    path('person/new', views.new_person, name='new person')
]
