from django.db import models
from django.core.validators import EmailValidator, MinLengthValidator
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)  # Example max_length constraint
    email = models.EmailField(max_length=100, unique=True, validators=[EmailValidator()])  # Email validation
    password = models.CharField(max_length=16, validators=[MinLengthValidator(8)])  # Password with minimum length constraint

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)