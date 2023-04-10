from django.urls import path

from . import views

app_name = 'instances'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:instance_id>/', views.detail, name='instances'),
]
