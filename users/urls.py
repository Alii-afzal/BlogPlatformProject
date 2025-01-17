from django.urls import path
from . import views

urlpatterns = [

    path('authors/', views.author_list, name="author_list"),
    path('authors/<int:pk>/', views.author_details, name="author_details"),
    path('login/', views.login_view, name='login'),
    path('author_admin/', views.author_admin, name='author_admin'),

]