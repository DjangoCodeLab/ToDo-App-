from django.contrib import admin
from django.urls import path
from todo import views
urlpatterns = [
    path('', views.index , name = 'todo'),
    path('data', views.read_data, name = 'data'),
    path('delete_data/<id>/', views.delete_data, name = 'delete_data'),
    path('update_data/<int:id>/', views.update_data, name = 'update_data')
    
    
]
