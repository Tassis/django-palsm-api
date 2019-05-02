"""
Comments url file.
"""
from django.urls import path, include

from .views import CommentsView, CommentDetailView

urlpatterns = [
    path('', CommentsView.as_view()),
    # path('<int:pk>/', CommentDetailView.as_view())
]
