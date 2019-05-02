"""
Pages route file.
"""
from django.urls import path, include

from .views import PageView, PageDetailView

urlpatterns = [
    path('', PageView.as_view()),
    path('<int:pk>/', PageDetailView.as_view())
]