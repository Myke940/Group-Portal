from django.urls import path
from .views import GroupProfileDetail, UserProfileView
urlpatterns = [

path('', GroupProfileDetail.as_view(), name='group-detail'),
path('user/profile/', UserProfileView.as_view(), name='user-profile'),




]