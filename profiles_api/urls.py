from django.urls import path
from profiles_api import views

urlpatterns = [
    path('hello-view/<int:pk>/', views.HelloApiView.as_view(), name='hello-api-view'),
]