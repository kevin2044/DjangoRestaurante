from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products')
    """ los 5 digitos abarca valor y decimales ejemplo 999.99 """
    price = models.DecimalField(max_digits=5, decimal_places=2)
    active = models.BooleanField(default=False)
    category = models.ForeignKey('categories.Category', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.title