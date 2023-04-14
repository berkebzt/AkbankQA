from django.db import models
from autoslug import AutoSlugField
from blog.models import CategoryModel

class WriteModel(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from = 'title', unique=True)
    categories = models.ManyToManyField(CategoryModel, related_name='writing')