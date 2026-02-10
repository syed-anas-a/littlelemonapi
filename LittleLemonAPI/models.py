from django.db import models

# Create your models here.
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title