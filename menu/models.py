from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Menu(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_menu')
    date = models.DateField(unique=True)
    breakfast = models.TextField()
    lunch = models.TextField()
    dinner = models.TextField()
    voter = models.ManyggToManyField(User, related_name='voter_menu')
    
    def __str__(self):
        return self.breakfast
