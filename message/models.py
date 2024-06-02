from django.db import models

class message(models.Model):
    text = models.CharField(max_length=225)
    def __str__(self):
        return self.text