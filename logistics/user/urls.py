from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('enter_code/', views.enter_code, name='enter_code'),
    path('timeline/<str:code>/', views.package_timeline, name='package_timeline'),
]