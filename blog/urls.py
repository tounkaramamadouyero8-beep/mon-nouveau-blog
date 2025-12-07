from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('message/', views.create_message, name='message_form'),
    path('message_success/', views.message_success, name='message_success'),
]
