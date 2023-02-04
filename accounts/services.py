from typing import Protocol, OrderedDict
from accounts import models, repos

from django.db.models import QuerySet


class AccountsServicesInterface(Protocol):
    account_repos: repos.AccountReposInterface

    def get_accounts(self, action: str) -> QuerySet[models.Account]: ...

    def create_account(self, data: OrderedDict) -> None: ...


class AccountsServicesV1:
    account_repos: repos.AccountReposInterface = repos.AccountReposV1()

    def get_accounts(self, action: str) -> QuerySet[models.Account]:
        return self.account_repos.get_accounts(action=action)

    def create_account(self, data: OrderedDict) -> None:
        self.account_repos.create_account(data=data)
