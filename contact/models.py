from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Contact(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    phone = models.CharField( max_length=50)
    email = models.EmailField(max_length=150)
    date = models.DateTimeField( auto_now_add=True)
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        
        return f"{self.firstname} {self.lastname}"
    