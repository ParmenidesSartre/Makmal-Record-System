from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('makmal/rekod/', views.makmal , name = 'makmal'),
    path('makmal/edit/<int:pk>/', views.edit_report , name = 'editreport'),
    path('makmal/add/', views.add_record , name = 'addreport'),
    path('makmal/print/<int:pk>/', views.print_report, name= 'printreport')
]