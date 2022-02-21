from django.urls import path
from .views import HomePageView, PostDetailView , AddPostView


app_name = 'feed'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('info/<int:pk>/', PostDetailView.as_view(), name = 'details'),
    path('post/', AddPostView.as_view(), name = 'post'),
] 
