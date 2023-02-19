from django.urls import path
from .views import *
from . import views

urlpatterns = [
   path('',views.index, name='index'),
   path('post/<int:pk>',views.Blog_detail, name='detail'),
   path('new_post/',CreatePost.as_view(), name='new_post'),
   path('posts/update/<int:pk>',UpdatePost.as_view(), name='update_post'),
   path('posts/<int:pk>/delete',DeletePost.as_view(), name='delete_post'),
   path('new_category/',CreateCategory.as_view(), name='new_category'),
]
