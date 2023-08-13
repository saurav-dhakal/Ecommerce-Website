from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contact/', views.contact, name='contact'),
    path('privacypolicy/', views.privacypolicy, name='privacypolicy'),
    path('deliverypolicy/', views.deliverypolicy, name='deliverypolicy'),
    path('folder/', views.folder, name='folder'),
    path('orderform/<int:id>', views.orderform, name='orderform'),
    path('orderfolder/<int:id>', views.orderfolder, name='orderfolder'),

    path('test/', views.test, name='test'),
]
