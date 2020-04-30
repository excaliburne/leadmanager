from django.db import models
from django.contrib.auth.models import User

class Lead(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="leads", null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
        
