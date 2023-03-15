from django.urls import path
from . import views

app_name = 'marketapp'

urlpaterns = [ 
    path('', views.index, name='index'),
    path('<int:pk>/', views.item_detail, name='item_detail'),
]