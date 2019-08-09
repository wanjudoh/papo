from django.db import models

# Create your models here.


class Tip(models.Model):
    guicha = '귀차니즘'
    sigan = '시간절약'
    ganzi = '폭풍간지'
    GROUP_CHOICES = [
    (guicha,'귀차니즘'),
    (sigan,'시간절약'),
    (ganzi,'폭풍간지'),
]
    group = models.CharField(max_length=10, choices= GROUP_CHOICES)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')
    notion = models.CharField(max_length=1000, null=True)
    #hits = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

class HitCount(models.Model):
    ip = models.CharField(max_length=15, default=None, null=True)
    post = models.ForeignKey(Tip, on_delete=models.CASCADE, default=None, null=True)


class Suggest(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title