from django.db import models
from autoslug import AutoSlugField

class CategoryModel(models.Model):
    name = models.CharField(max_length=30, blank=False,null=False)
    slug = AutoSlugField(populate_from = 'name',unique=True)