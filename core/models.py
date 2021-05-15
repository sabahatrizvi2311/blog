from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=30)
    date = models.DateTimeField()
    content = models.TextField(max_length=1000)
    writer = models.CharField(max_length=30)
    slug = models.SlugField()
    image = models.ImageField(upload_to='static/images/', default='', blank=True, null=True)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("core:blog", kwargs={
            'slug': self.slug
        })


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    comment_date = models.DateTimeField()
    comment = models.TextField()