from django.urls import path

from .views import *

urlpatterns = [
    path('v1/womenlist/', WomenAPIList.as_view()),
    path('v1/womenlist/<int:pk>/', WomenAPIList.as_view()),
]