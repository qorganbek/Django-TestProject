from django.db.models import Q
from django_filters import rest_framework as filters
from accounts import models


class WalletFilter(filters.FilterSet):
    firstName = filters.CharFilter(field_name='account__firstName', lookup_expr='icontains')
    lastName = filters.CharFilter(field_name='account__lastName', lookup_expr='icontains')
    name = filters.CharFilter(method='filter_name')

    class Meta:
        model = models.Wallet
        fields = ['firstName', 'lastName', 'account', 'name', 'amount']

    def filter_name(self, queryset, _, value):
        return queryset.filter(
            Q(account__firstName=value) | Q(account__lastName=value)
        )


class AccountFilter(filters.FilterSet):
    firstName = filters.CharFilter(field_name='firstName', lookup_expr='icontains')
    lastName = filters.CharFilter(field_name='lastName', lookup_expr='icontains')

    class Meta:
        model = models.Account
        fields = ['firstName', 'lastName']

