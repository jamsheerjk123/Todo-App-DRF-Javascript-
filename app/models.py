from django.db import models

# Create your models here.
class Todo(models.Model):

    

    title = models.CharField(max_length=60,blank=False,null=False)
    description = models.TextField(max_length=260)
    completed=models.BooleanField(default=False,blank=True,null=True)


    def __str__(self):
        return self.title