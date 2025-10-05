from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinLengthValidator

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile__pics/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username} 's profile page"

#handles creation of user profile when a new user is created
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance) 

#saves user profile when user instance is saved
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_save, sender=User) #signal to create or update user profile
def create_or_update_user_profile(sender, instance, created, **kwargs): # when a user is created or updated
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name= 'comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000, validators=[MinLengthValidator(3)], blank=False, null=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"comment by {self.author}"

# Create your models here.
