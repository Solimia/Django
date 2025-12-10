
from django.db import models


class Beauty(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    opening_date = models.DateField()

    def __str__(self):
        return self.name


class Service(models.Model):
    salon = models.ForeignKey(Beauty, on_delete=models.CASCADE, related_name="services")
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    duration_minutes = models.IntegerField()

    def __str__(self):
        return f"{self.name} — {self.price} грн"


class Master(models.Model):
    salon = models.ForeignKey(Beauty, on_delete=models.CASCADE, related_name="masters")
    name = models.CharField(max_length=100)
    experience_years = models.IntegerField()
    phone = models.CharField(max_length=20)
    services = models.ManyToManyField(Service, related_name="masters")

    def __str__(self):
        return f"{self.name} ({self.experience_years} років досвіду)"
