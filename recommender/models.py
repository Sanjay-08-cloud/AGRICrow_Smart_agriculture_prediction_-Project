from django.db import models
from django.contrib.auth.models import User

class PredictionHistory(models.Model):
    STATUS_CHOICES = [
        ('Recommended', 'Recommended'),
        ('Cultivation', 'Cultivating'),
        ('Harvested', 'Harvested'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='predictions')
    n = models.FloatField(verbose_name="Nitrogen (N)")
    p = models.FloatField(verbose_name="Phosphorus (P)")
    k = models.FloatField(verbose_name="Potassium (K)")
    temperature = models.FloatField(verbose_name="Temperature (°C)")
    humidity = models.FloatField(verbose_name="Humidity (%)")
    ph = models.FloatField(verbose_name="pH Level")
    rainfall = models.FloatField(verbose_name="Rainfall (mm)")
    predicted_crop = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Recommended')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} predicted {self.predicted_crop} at {self.created_at.strftime('%Y-%m-%d %H:%M')}"

