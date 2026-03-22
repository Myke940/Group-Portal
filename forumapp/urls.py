from django.urls import path
from .views import PostCreateView, PostDetailView, PostListView, VoteView, CommentCreateView, RegisterView, ChatView, LoginView, LogoutView, Aboutus










urlpatterns = [
    path("Announcements/", PostListView.as_view(), name = "index"),
    path("post/<int:pk>/", PostDetailView.as_view(), name = "post_detail"),
    path("post/<int:post_id>/comment/", CommentCreateView.as_view(), name = "add_comment"),
    path("vote/<int:post_id>/", VoteView.as_view(), name = "vote"),
    path("post/create/", PostCreateView.as_view(), name = "post_create"),
    path('chat/', ChatView.as_view(), name = 'chat1'),
    path("about_us/", Aboutus.as_view(), name="about_us"),
    
    
]

