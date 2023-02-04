from typing import Protocol, OrderedDict

from django.db import transaction
from django.db.models import QuerySet, Sum, Avg, Case, When, F, DecimalField, Q
from decimal import Decimal
from accounts import models, constants


class AccountReposInterface(Protocol):
    def get_accounts(self, action: str) -> QuerySet[models.Account]: ...

    def create_account(self, data: OrderedDict) -> None: ...


class AccountReposV1:
    def get_accounts(self, action: str) -> QuerySet[models.Account]:
        accounts = models.Account.objects.all()

        if action not in ('list', 'retrieve'):
            return accounts

        return accounts.prefetch_related('wallets').annotate(
            total_sum=Sum(
                'wallets__amount',
                default=Decimal(0.0),
                filter=Q(wallets__amountCurrency__in=(constants.AmountCurrencyChoices.KZT, constants.AmountCurrencyChoices.USD))
            ),
            avg_amount=Avg('wallets__amount', default=Decimal(0.0)),
            custom_amount=Sum(
                Case(
                    When(Q(wallets__amountCurrency=constants.AmountCurrencyChoices.USD), then=F('wallets__amount') * 2),
                    When(Q(wallets__amountCurrency=constants.AmountCurrencyChoices.KZT), then=F('wallets__amount') * 500),
                    default=Decimal(0.0),
                    output_field=DecimalField()
                )
            )
        ).all()

    def create_account(self, data: OrderedDict) -> None:
        with transaction.atomic():
            wallets = data.pop('wallets')
            account = models.Account.objects.create(**data)
            raise AttributeError
            models.Wallet.objects.bulk_create([models.Wallet(**w, account=account) for w in wallets])

