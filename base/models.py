from django.db import models
from django.contrib.auth.models import User


class Shedule(models.Model):
    class Priority(models.IntegerChoices):
        LOW = 1, "Low"
        MEDIUM = 2, "Medium" 
        HIGH = 3, "High"

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    priority = models.IntegerField(choices=Priority.choices, default=Priority.MEDIUM)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title