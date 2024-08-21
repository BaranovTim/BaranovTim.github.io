from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField('Title',max_length=100)
    content = models.TextField('Text',max_length=1000)
    date = models.DateField('Date',auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField('Image', null=True, blank=True, upload_to='main/static/main/img')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'