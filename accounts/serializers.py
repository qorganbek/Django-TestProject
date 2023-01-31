from rest_framework import serializers
from accounts import models


class _AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = ['firstName', 'lastName']


class WalletSerializer(serializers.ModelSerializer):
    account = _AccountSerializer(read_only=True, many=False)

    class Meta:
        model = models.Wallet
        fields = '__all__'


class _WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Wallet
        fields = ['amount', 'amountCurrency']


class AccountSerializer(serializers.ModelSerializer):
    wallets = _WalletSerializer(write_only=True, many=True)
    total_sum = serializers.DecimalField(read_only=True, max_digits=14, decimal_places=2)
    avg_amount = serializers.DecimalField(read_only=True, max_digits=14, decimal_places=2)
    custom_amount = serializers.DecimalField(read_only=True, max_digits=14, decimal_places=2)

    class Meta:
        model = models.Account
        fields = '__all__'


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Restaurant
        fields = '__all__'


class PlaceSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer(read_only=True, many=False)

    class Meta:
        model = models.Place
        fields = '__all__'


class AccountSerializerV2(serializers.ModelSerializer):
    wallets = _WalletSerializer(read_only=True, many=True)

    class Meta:
        model = models.Account
        fields = '__all__'