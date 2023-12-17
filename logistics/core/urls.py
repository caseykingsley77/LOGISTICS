from django.urls import path
from . import views

urlpatterns = [
    path('', views.package_info, name='package_info'),
    path('<int:package_id>/update_location/', views.update_package_location, name='update_package_location'),
    path('<int:package_id>/timeline/', views.package_timeline, name='package_timeline'),
    path('generate/', views.generate_package_code, name='generate_package_code'),
    path('<int:package_id>/', views.package_detail, name='package_detail'),
]