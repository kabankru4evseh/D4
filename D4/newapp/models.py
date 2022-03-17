from django.db import models


class New(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} {self.text}'

