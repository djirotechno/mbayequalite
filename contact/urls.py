from django.urls import path
from .views import home, about, services,contact,reference,formation,team

urlpatterns = [
   
    path("",home,name="home"),
    path("about/",about,name="about"),
    path("service/",services,name="services"),
    path("fererence/",reference,name="reference"),
    path("formation/",formation,name="formation"),
    path("team/",team,name="team"),
    path("contact/",contact,name="contact"),
    
]