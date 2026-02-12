from django.db import models

# Create your models here.
class MenuItem(models.Model):

    category_choices = [
        ('appetizer', 'Appetizer'),
        ('main_course', 'Main Course'),
        ('dessert', 'Dessert'),
        ('beverage', 'Beverage'),
    ]

    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    category = models.CharField(choices=category_choices, max_length=25, default=category_choices[1][1])
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title