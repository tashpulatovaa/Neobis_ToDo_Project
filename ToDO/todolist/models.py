from django.db import models

# Create your models here.

class ToDo(models.Model):
    title = models.CharField('Title of the task', max_length=200)
    description = models.CharField('Description', max_length=600)
    is_complete = models.BooleanField('Done', default=False)

    class Meta:
        verbose_name = 'Title'
        verbose_name_plural = 'Titles'

    def __str__(self):
        return self.title