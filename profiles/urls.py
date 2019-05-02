"""
Profiles route file.
"""
from django.urls import path
from .views import ProfilesList, ProfilesDetail

urlpatterns = [ 
    path('', ProfilesList.as_view()),
    path('<int:key>/', ProfilesDetail.as_view())
]
