from django.db import models
from django.contrib.auth.models import User

#from django.contrib.auth import get_user_model
# Create your models here.

class Market(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')
    pub_date = models.DateTimeField(auto_now_add=True)
    summary = models.CharField(null=True, max_length=100)
    body = models.TextField(default='')
    image = models.ImageField(null=True, upload_to='images/')
    pptfile = models.FileField(null=True, upload_to='documents/')
    users = models.ManyToManyField(User, related_name='users', through='Scrap')
    
    def __str__(self):
        return self.title

    def total_scraps(self):
        return self.users.count()


class Scrap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Market, on_delete=models.CASCADE)
    scrap_date = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.post.title