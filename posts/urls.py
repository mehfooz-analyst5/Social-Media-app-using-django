from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
   
    path("create/", views.post_creation, name="post_creation"),

    

]
