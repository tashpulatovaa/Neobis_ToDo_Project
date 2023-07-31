from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
    
    def __str__(self):
        return self.title
