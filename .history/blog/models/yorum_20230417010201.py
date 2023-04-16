from django.db import models
from django.contrib.auth.models import User
from blog.models import WriteModel
from blog.abstract_models import DateAbstractModel
class CommentModel(DateAbstractModel):
    yazan = models.ForeignKey('account.CustomUserModel', on_delete = models.CASCADE, related_name = 'comment')
    writing = models.ForeignKey(WriteModel, on_delete = models.CASCADE, related_name='comments')
    comment = models.TextField()
   
    
    class Meta:
        db_table ='comment'
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
        
    def __str__(self):
        return self.yazan.username    