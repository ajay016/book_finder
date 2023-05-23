from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    no_of_copies = models.IntegerField(default=1, null=True, blank=True)
    status = models.CharField(max_length=15, choices=[('Out of Stock', 'Out of Stock'), ('Available', 'Available')], default='Available')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Author(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name
    

class Genre(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    books = models.ManyToManyField(Book)
    
    def __str__(self):
        return self.name
