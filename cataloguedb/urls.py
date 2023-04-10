from django.urls import path

from . import views

app_name = 'catalogue'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:instance_id>/', views.detail, name='detail'),
]
