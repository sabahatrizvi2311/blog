from django.urls import path
from .views import *


app_name = 'core'

urlpatterns = [
    path('', BlogsList.as_view(), name='bloglist'),
    path('<slug:slug>/', BlogDetails.as_view(), name='blog'),
] 