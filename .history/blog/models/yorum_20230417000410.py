from django.db import models
from django.contrib.auth.models import User
from blog.models import WriteModel

class CommentModel(models.key):
    yazan = models.ForeignKey(User, on_delete = models.CASCADE, relate_name = 'comment')
    writing = models.ForeignKey(WriteModel, on_delete = models.CASCADE, related_name='comments')
    comment = models.TextField()
    create_time = models.DateTimeField(auto_now_add = True)
    edit_time = models.DateTimeField(auto_now = True)
    