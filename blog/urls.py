from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_of_post, name='list_of_post'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('category/<slug:category_slug>/', views.list_of_post_by_category, name='list_of_post_by_category'),
    path('main/',views.maninmenu,name='mainmenu'),
    #path('<slug:slug>/comment/', views.add_comment, name='add_comment'),

    #backend urls
    path('backend/post/new/',views.new_post, name='new_post'),
    path('backend/post/',views.list_of_post_backend, name='list_of_post_backend'),
    path('backend/post/<slug:slug>/edit/', views.edit_post, name='edit_post'),
    path('backend/post/<slug:slug>/delete/', views.delete_post, name='delete_post'),
]