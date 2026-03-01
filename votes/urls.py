from django.urls import path
from . import views

app_name = 'voting'
urlpatterns = [
    path('', views.VoteListView.as_view(), name='vote_list'),
    path('<int:pk>/', views.VoteDetailView.as_view(), name='vote_detail'),
    path('create/', views.VoteCreateView.as_view(), name='vote_create'),
    path('<int:pk>/vote/', views.VoteCastView.as_view(), name='vote_cast'),
]