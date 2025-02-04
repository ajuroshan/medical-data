"""
organisation/urls.py
"""

from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home),
    path('user/', views.hello),

]
