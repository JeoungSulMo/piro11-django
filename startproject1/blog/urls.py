from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_detail, name='post_detail'),
    # path('create/', views.create, name="create"),
    path('post/new/', views.post_new, name="post_new"),
    path('post/edit/<int:id>', views.post_edit, name="post_edit"),

]
