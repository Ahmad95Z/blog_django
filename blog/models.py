from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField( max_length=100)
    url = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'



class Post(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(null=True, blank=True, upload_to='articles/')
    body = RichTextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category , on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        return reverse('index')

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=670)
    create_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.author)

    

class Profile(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    instagram_url = models.CharField(max_length=150, blank=True, null=True) 
    body = models.TextField()
    profile_image = models.ImageField(null=True, blank=True, upload_to='articles/profile/')

    
    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('index')