from django.db import models

# Create your models here.
class newsUpdate(models.Model):
    title = models.CharField(max_length=150)
#    slug  = models.SlugField()
    body  = models.TextField()
    date  = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    file  = models.FileField(blank=True, null=True, upload_to="file")


class noticeUpdate(models.Model):
    title = models.CharField(max_length=150)
    body  = models.TextField(max_length=500)
    date  = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    file  = models.FileField(blank=True, null=True, upload_to="file")
    thumb = models.ImageField(default='default.png', blank=True)



    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:0] + '...'
