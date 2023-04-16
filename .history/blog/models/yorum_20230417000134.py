from django.db import models
from django.contrib.auth.models import User

class CommentModel(models.key):
    yazan = models.ForeignKey(User, on_delete = models.CASCADE)
    