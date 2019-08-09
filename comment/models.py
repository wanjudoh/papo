from django.db import models
from market.models import Market
from django.contrib.auth.models import User
#세션때는 post 모델 임포트 해오는데 우리는 마켓에 쓸거니까 이거 맞나?

# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(Market, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content