from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views


urlpatterns = [
    path('public/', views.public_test),
    path('private/', views.private_test),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    ]
