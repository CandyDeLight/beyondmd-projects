from django.urls import path
from . import views

# all of my URLs are here
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('addToDatabase/', views.addToDatabase, name='addToDatabase'),
    path('profile/deleteFromDatabase/', views.deleteFromDatabase, name='deleteFromDatabase'),
    path('profile/updateToDatabase/', views.updateToDatabase, name='updateToDatabase')
]