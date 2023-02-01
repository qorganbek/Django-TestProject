from django.db import models
from accounts import constants


class Account(models.Model):
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='accounts/', blank=True, null=True)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'


class Wallet(models.Model):
    account = models.ForeignKey(to=Account, on_delete=models.CASCADE, related_name='wallets')
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    amountCurrency = models.CharField(max_length=3, choices=constants.AmountCurrencyChoices.choices, default='KZT')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.account} {self.amount} {self.amountCurrency}'


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return "%s the place" % self.name


class Restaurant(models.Model):
    place = models.OneToOneField(
        to=Place,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='restaurant',
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant" % self.place.name
