from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=60)
    content = models.CharField(max_length=20)
    def __str__(self):
        return self.name
