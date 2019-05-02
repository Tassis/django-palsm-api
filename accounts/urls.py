from django.urls import include, path
from accounts.views import AccountDetail

urlpatterns = [
    path('detail/', AccountDetail.as_view()),
    path('register/', include('rest_auth.registration.urls'))
]