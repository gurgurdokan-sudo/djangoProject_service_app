from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('users/user_create', views.user_create, name='create'),
    path('users/<int:user_id>/export/<int:year>/<int:month>/', \
     views.export_service_sheet, name='export_service_sheet'),
    path('user/<int:user_id>/detail/', views.user_detail, name='detail'),
    path('user/<int:user_id>/edit/', views.user_update, name='update'),
    path('user/<int:user_id>/delete/', views.user_delete, name='delete'),
    path('user/<int:user_id>/service/', views.user_service, name='service'),
    path('user/<int:user_id>/test/', views.test, name='test'),
]