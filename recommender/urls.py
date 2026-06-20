from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.prediction_dashboard, name='prediction_dashboard'),
    path('update-status/', views.update_prediction_status, name='update_prediction_status'),
    path('crop-dataset/', views.crop_dataset_view, name='crop_dataset'),
    path('ml-analytics/', views.ml_analytics_view, name='ml_analytics'),
]

