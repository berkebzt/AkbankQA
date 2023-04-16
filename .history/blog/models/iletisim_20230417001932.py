from django.db import models


class CommunicationModel(models.Model):
    email = models.EmailField(max_length=250)
    name_surname = models.CharField(max_length = 150)
    message = models.TextField()
    
    class Meta:
        db_table = 'communication'
        verbose_name = 'Communication'
        verbose_name_plural = 'Communications'
        
    def __str__(self):
        return self.email     