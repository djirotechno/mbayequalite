"impor module"
from django.shortcuts import render



# Create your views here.

def home(request):
    "home function return index page"

    return render(request,"pages/index.html")


def about(request):
    "home function return about page"
    msg = "About"
    return render(request,"pages/about.html",context={'msg':msg})

def services(request):
    "home function return services page"
    msg = "Service"
    return render(request,"pages/services.html",context={'msg':msg})

def contact(request):
    "home function return formation page"
    return render(request,"pages/contact.html")


def reference(request):
    "home function return formation page"
    return render(request,"pages/portfolio.html")

def equipe(request):
    "home function return formation page"
    return render(request,"pages/team.html")

def formation(request):
    "formation function"
    return render(request,"pages/blog.html")

def team(request):
    "formation function"
    return render(request,"pages/team.html")




# End-of-file (EOF)