from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # path('post/new', views.post_new, name='post_new'),
    # path('blog/writing_page/', views.writing_page, name='writing_page'),
    # path('blog/create/',views.create, name='create'),
]
