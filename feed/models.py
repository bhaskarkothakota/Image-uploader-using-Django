from django.db import models
from sorl.thumbnail import ImageField



# Create your models here.
class post(models.Model):
    text = models.CharField(max_length=140, blank=False, null=False)
    image = ImageField()
    

    def __str__(self):
        ImageField
        return self.text