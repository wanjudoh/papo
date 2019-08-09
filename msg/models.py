from django.db import models

# Create your models here.
class Msg(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(default='')
    link = models.CharField(max_length=500)
    image = models.ImageField(null=True, upload_to='msg/')
    
    color = 'color'
    img = 'img'
    template = 'template'
    font = 'font'
    GROUP_CHOICES = [(color,'color'), (img,'img'), (template,'template'),(font, 'font')]
    
    group = models.CharField(max_length=10, choices= GROUP_CHOICES, null=True)
    
    def __str__(self):
        return self.title
