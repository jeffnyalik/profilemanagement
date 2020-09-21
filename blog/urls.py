from django.urls import path
from .import views
from .views import ListPostView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,UserListPostView

urlpatterns = [
    path('', ListPostView.as_view(), name='blog-home'),
    path('user/<str:username>', views.UserListPostView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-details'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('index/', views.index, name='blog-index'),
]

