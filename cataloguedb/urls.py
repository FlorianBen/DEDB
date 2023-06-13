from django.urls import path

from . import views

app_name = 'catalogue'
urlpatterns = [
    path('', views.index, name='index'),
    path('reference', views.index, name='reference'),
    path('reference/add', views.reference_add, name='reference_add'),
    path('reference/<int:instance_id>/', views.detail, name='detail'),
    path('manufacturer', views.index_manufacturers, name='manufacturer'),
    path('manufacturer/add', views.manufacturer_add, name='manufacturer_add'),
    path('manufacturer/<int:instance_id>/', views.detail_manufacturers, name='detail_manufacturer'),
]

hmtx_views = [
    path("add-manufacturer/", views.add_manufacturer, name='add-manufacturer'),
    path("add-reference/", views.add_reference, name='add-reference'),
    path("filter-manufacturer/", views.filter_manufacturer, name='filter-manufacturer'),
]

urlpatterns += hmtx_views
