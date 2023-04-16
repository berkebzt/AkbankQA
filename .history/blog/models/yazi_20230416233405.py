from django.db import models
from autoslug import AutoSlugField
from blog.models import CategoryModel
from django.contrib.auth.models import User

class WriteModel(models.Model):
    img = models.ImageField( upload_to='writing_images')
    title = models.CharField(max_length=50)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from = 'title', unique=True)
    categories = models.ManyToManyField(CategoryModel, related_name='writing')
    writer = models.ForeignKey(User,on_delete=models.CASCADE, related_name='writings')
    
    class Meta:
        verbose_name='Writing'
        verbose_name_plural='Writings'
        db_table = 'Writing'  