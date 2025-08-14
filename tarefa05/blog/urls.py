from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Post/<int:id>/', views.detalhe_post, name= 'detalhe_post'),
]
