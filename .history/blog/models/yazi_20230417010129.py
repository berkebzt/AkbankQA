from django.db import models
from autoslug import AutoSlugField
from blog.models import CategoryModel
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from blog.abstract_models import DateAbstractModel
class WriteModel(DateAbstractModel):
    img = models.ImageField( upload_to='writing_images')
    title = models.CharField(max_length=50)
    content = RichTextField()
    
    slug = AutoSlugField(populate_from = 'title', unique=True)
    categories = models.ManyToManyField(CategoryModel, related_name='writing')
    writer = models.ForeignKey('account.CustomUserModel',on_delete=models.CASCADE, related_name='writings')
    
    class Meta:
        verbose_name='Writing'
        verbose_name_plural='Writings'
        db_table = 'Writing'  
        
    def __str__(self):
        return self.title    