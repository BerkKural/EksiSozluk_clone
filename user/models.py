from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name= 'İsim')
    surname = models.CharField(max_length=100, verbose_name= 'Soyisim')
    bio = models.TextField(max_length=500, verbose_name= 'Hakkımda', default='Merhaba, ben bir blog yazarıyım')
    image = models.FileField(upload_to='profiles/', null=True, verbose_name='Porfil Resmi', default='static/profiles/defaultpp.jpg')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name= 'Oluşturulma Tarihi', null=True)
    follow = models.ManyToManyField('self', verbose_name= 'Takip', blank=True)
    followers = models.ManyToManyField('self', verbose_name= 'Takipçiler', blank=True)

    def __str__(self):
        return self.user.username