from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    published_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField('Book', )

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField('Library', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    
    RoleChoices = [
        ('Admin','Admin'),
        ('Librarian','Librarian'),
        ('Member', 'Member'),  
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices = RoleChoices, default='Member')

    def __str__(self):
        return f"{self.user.username}, {self.role}"

class Meta(Book):
    permissions = [
        ("can_add_book", "Can add book"),
        ("can_change_book", "Can change book"),
        ("can_delete_book", "Can delete book"),
    ]    
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, role='Member')

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

# Create your models here.
