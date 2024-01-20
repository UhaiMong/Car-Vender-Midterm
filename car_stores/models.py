from django.db import models
from django.contrib.auth.models import User as AuthUser

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Car(models.Model):
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, related_name='cars')
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()
    model_name = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='car_stores/media/uploads/', blank=True, null=True)

    def __str__(self):
        return f"{self.year} {self.brand} {self.model_name}"


class Purchase(models.Model):
    buyer = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.buyer.username} purchased {self.car}"


class Comment(models.Model):
    car = models.ForeignKey(
        Car, on_delete=models.CASCADE, related_name='comments')
    commenter_name = models.CharField(max_length=100)
    comment_text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.commenter_name} commented on {self.car}"
