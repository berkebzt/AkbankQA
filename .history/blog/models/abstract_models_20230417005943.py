from django.db import models

class DateAbstractModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)