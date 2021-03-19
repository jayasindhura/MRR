from django.conf.urls import url
from . import views
from django.urls import path, re_path
from mymrr.views import *

app_name = 'mymrr'
urlpatterns = [

    path("", homepage, name='homepage'),
    path('home_reviewer/', views.home_reviewer, name='home_reviewer'),
    path('home_staff/', views.home_staff, name='home_staff'),

    path("staff-login/", staffLogin, name='staffLogin'),
    path("reviewer-login/", reviewerLogin, name='reviewerLogin'),

    path("staff-signup/", staffSignup, name='staffSignup'),
    path("reviewer-signup/", reviewerSignup, name='reviewerSignup'),

    path("logout/", user_logout, name='user_logout'),

    re_path(r'^home/$', views.home, name='home'),
    path('reviewer_list', views.reviewer_list, name='reviewer_list'),
    path('reviewer_list_staff', views.reviewer_list_staff, name='reviewer_list_staff'),

    path('reviewer_staff/create/', views.reviewer_new_staff, name='reviewer_new_staff'),

    path('reviewer/<int:pk>/edit/', views.reviewer_edit, name='reviewer_edit'),
    path('reviewer_staff/<int:pk>/edit/', views.reviewer_edit_staff, name='reviewer_edit_staff'),

    path('reviewer/<int:pk>/delete/', views.reviewer_delete, name='reviewer_delete'),
    path('reviewer_staff/<int:pk>/delete/', views.reviewer_delete_staff, name='reviewer_delete_staff'),

    path('movie_ratings_list', views.movie_ratings_list, name='movie_ratings_list'),
    path('movie_ratings_list_staff', views.movie_ratings_list_staff, name='movie_ratings_list_staff'),

    path('movie_ratings/create/', views.movie_ratings_new, name='movie_ratings_new'),
    path('movie_ratings_staff/create/', views.movie_ratings_new_staff, name='movie_ratings_new_staff'),

    path('movie_ratings/<int:pk>/edit/', views.movie_ratings_edit, name='movie_ratings_edit'),
    path('movie_ratings_staff/<int:pk>/edit/', views.movie_ratings_edit_staff, name='movie_ratings_edit_staff'),

    path('movie_ratings/<int:pk>/delete/', views.movie_ratings_delete, name='movie_ratings_delete'),
    path('movie_ratings_staff/<int:pk>/delete/', views.movie_ratings_delete_staff, name='movie_ratings_delete_staff'),

    path('movie_list', views.movie_list, name='movie_list'),
    path('movie_list_staff', views.movie_list_staff, name='movie_list_staff'),

    path('movie/create/', views.movie_new, name='movie_new'),
    path('movie_staff/create/', views.movie_new_staff, name='movie_new_staff'),

    path('movie/<int:pk>/edit/', views.movie_edit, name='movie_edit'),
    path('movie_staff/<int:pk>/edit/', views.movie_edit_staff, name='movie_edit_staff'),

    path('movie/<int:pk>/delete/', views.movie_delete, name='movie_delete'),
    path('movie_staff/<int:pk>/delete/', views.movie_delete_staff, name='movie_delete_staff'),

    path('pdf/', views.movie_ratings_summary_pdf,name='movie_ratings_summary_pdf'),

    #path('movie_ratings_summary_pdf', views.movie_ratings_summary_pdf, name='movie_ratings_summary_pdf'),

    #path('movie_ratings_summary_pdf', views.get, name='movie_ratings_summary_pdf'),
]
