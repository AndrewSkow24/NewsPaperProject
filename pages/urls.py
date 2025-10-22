from django.urls import path
from .views import HomePageView, test_email

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("test-email/", test_email, name="test_email"),
]
