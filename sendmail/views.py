from django.shortcuts import render

# Create your views here.
def sendmail(request):
    "home function return formation page"
    return render(request,"pages/contact.html")

