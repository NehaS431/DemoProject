from django.urls import path
from . import views
from .views import LoginView , RegisterUserAPIView , UpdateUserView ,ViewUser
# # from .views import MyTokenObtainPairView

# from rest_framework_simplejwt.views import (
#     TokenRefreshView,
# )

urlpatterns=[
    path('login/',LoginView.as_view(),name='LoginView'),
    path('register/',RegisterUserAPIView.as_view(),name='RegisterUserAPIView'),
    path('updateuser/',UpdateUserView.as_view(),name='UpdateUserView'),
    path('viewuser/',ViewUser.as_view(),name='ViewUser')
]