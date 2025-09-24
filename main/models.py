from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('shoes', 'Shoes'),
        ('ball', 'Ball'),
        ('jersey', 'Jersey'),
    ]
    
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='transfer')
    quantity = models.PositiveIntegerField(default=5)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    def get_name(self):
        return self.name
    
