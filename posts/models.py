from django.contrib.auth import get_user_model
from django.db import models
from services.utils import create_slug

User = get_user_model()


# Create your models here.
class Post(models.Model):
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    image = models.ImageField(upload_to='post_img/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = create_slug(self, self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']
