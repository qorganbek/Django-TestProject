from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination
from rest_framework.viewsets import ModelViewSet
from accounts import models, serializers, filters, services, pagination as pag


class AccountViewSet(ModelViewSet):
    account_services = services.AccountsServicesV1()
    # serializer_class = serializers.CreateAccountSerializer
    filterset_class = filters.AccountFilter
    pagination_class = pag.CustomPageNumberPagination

    # queryset = account_services.get_accounts(action=self.action)
    def get_queryset(self):
        return self.account_services.get_accounts(action=self.action)

    def get_serializer_class(self):
        # print(f'{self.action=}')
        if self.action in ('list', 'retrieve'):
            return serializers.RetrieveAccountSerializer

        return serializers.CreateAccountSerializer

    def perform_create(self, serializer: serializers.CreateAccountSerializer):
        self.account_services.create_account(data=serializer.validated_data)


class WalletViewSet(ModelViewSet):
    queryset = models.Wallet.objects.select_related('account', )
    serializer_class = serializers.WalletSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.WalletFilter


class PlaceViewSet(ModelViewSet):
    queryset = models.Place.objects.prefetch_related(
        'restaurant',
    )
    serializer_class = serializers.PlaceSerializer


class RestaurantViewSet(ModelViewSet):
    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.RestaurantSerializer


class AccountViewSetV2(ModelViewSet):
    account_services = services.AccountsServicesV1()
    # queryset = account_services.get_accounts()
    # serializer_class = serializers.RetrieveAccountSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.AccountFilter

    def get_serializer_class(self):
        # print(f'{self.action=}')
        if self.action in ('list', 'retrieve'):
            return serializers.RetrieveAccountSerializer

        return serializers.CreateAccountSerializer

    def get_queryset(self):
        return self.account_services.get_accounts(action=self.action)

    # def perform_create(self, serializer: serializers.AccountSerializer):
    #     self.account_services.create_account(data=serializer.validated_data)
