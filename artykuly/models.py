from django.db import models
from users.models import Account
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('users.Account', on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    zdjecie = models.ImageField(upload_to='articles/%Y/%m/%d', default='no_image.png')
    text = models.TextField(max_length=150)
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
