from django.urls import path
from . import views

app_name = 'subscription'

urlpatterns = [
    path('inscricao/', views.added_subscription, name='subscription'),
    path('subscription-list/', views.subscription_list, name='subscription-list'),
    path('<int:pk>/', views.subscription_detail, name='subscription-detail'),
    path('<int:pk>/', views.update_subscription, name='subscription-update'),
    path('<int:pk>/', views.delete_subscription, name='subscription-delete'),
]
