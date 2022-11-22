from django.urls import path
from . import views

# all of my URLs are here
urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('login_page/', views.login_page, name='login_page'),
    path('signup_page/', views.signup_page, name='signup_page'),
    path('index/', views.index, name='index'),
    path('index/logout_action/', views.logout_action, name='logout_action'),
    path('profile/', views.profile, name='profile'),
    path('profile/settings/', views.settings, name='settings'),
    path('index/addReviewToDatabase/', views.addReviewToDatabase, name='addReviewToDatabase'),
    path('profile/updateReviewToDatabase/', views.updateReviewToDatabase, name='updateReviewToDatabase'),
    path('profile/deleteReviewFromDatabase/', views.deleteReviewFromDatabase, name='deleteReviewFromDatabase')
]