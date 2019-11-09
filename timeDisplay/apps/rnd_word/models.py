from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return f"the movie object is : {self.title}"

class Wizard(models.Model):

    name = models.CharField(max_length=45)
    house = models.CharField(max_length=45)
    pet = models.CharField(max_length=45, null=True, blank=True, default=None)
    year = models.IntegerField()
    
    def __str__(self):
        return f"the wizards name is {self.name}"

class User(models.Model):

    username = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.SmallIntegerField(200)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username