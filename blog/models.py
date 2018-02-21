from django.db import models
from django.utils import timezone
import markdown


# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    content = models.TextField()
    content_html = models.TextField(editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-published_date', '-id']

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.content_html = markdown.markdown(self.content)
        super().save(*args, **kwargs)


class Image(models.Model):
    upload = models.ImageField(upload_to='blog/images/')
    description = models.TextField(blank=True, default='')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.description
