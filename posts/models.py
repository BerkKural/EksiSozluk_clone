from django.db import models
import uuid
from user.models import *
# Create your models here.
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Yazar')
    title = models.CharField(max_length=100, verbose_name='Başlık', null=True)
    content = models.TextField(max_length=500, null=True, verbose_name='İçerik')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    like = models.ManyToManyField(Profile, related_name='Likes', verbose_name='Beğenenler', blank=True)
    dislike = models.ManyToManyField(Profile, related_name='Dislikes', verbose_name='Beğenmeyenler', blank=True)
    isPublish = models.BooleanField(default=False, verbose_name='Yayınla')
    def __str__(self):
        return self.title