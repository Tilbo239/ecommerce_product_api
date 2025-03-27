from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


class Discount(models.Model):
    """
    The Discount class represents a discount on a product.
    """

    name = models.CharField(max_length=255, unique=True)
    percentage = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0.00,
    )
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def is_active(self):
        """Check if the discount is currently active."""
        now = timezone.localtime(timezone.now())
        return self.start_date <= now <= self.end_date

    def __str__(self):
        return f"{self.name} ({self.percentage}%) - Active: {self.is_active()}"
