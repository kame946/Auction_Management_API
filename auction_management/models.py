from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.

class Auction(models.Model):
    item_name = models.CharField(max_length=200)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField()
    start_price = models.DecimalField(max_digits=10, decimal_places=2)
    winner = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete=models.SET_NULL)

    def is_active(self):
        return self.end_time > timezone.now()
    
    def __str__(self):
        return self.item_name
