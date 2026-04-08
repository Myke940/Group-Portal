from django.urls import path
from .views import GroupProfileDetail, UserProfileView, UserEditor, RegisterView
urlpatterns = [

path('', GroupProfileDetail.as_view(), name='group-detail'),
path('user/profile/', UserProfileView.as_view(), name='user-profile'),
path('user/profile/Editor', UserEditor.as_view(), name = 'profile-edit'),
path('user/register', RegisterView.as_view(), name = 'register-profile'),


]