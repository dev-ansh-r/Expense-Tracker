from django.db import models

# Create your models here.
class expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        self.name