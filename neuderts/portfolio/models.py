from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50)
    subtitle = models.CharField(max_length=50, blank=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    #author

    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[:50]
