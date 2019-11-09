from django.db import models

class Book(models.Model):
    
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f"Title : {self.title} id is : {self.id}"

class Author(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    notes = models.TextField(null=True)
    books = models.ManyToManyField(Book, related_name='authors')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f"{self.first_name} {self.last_name} id is : {self.id}"
