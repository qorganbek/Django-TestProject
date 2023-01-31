from django.urls import path, include
from rest_framework import routers
from accounts import views

router = routers.DefaultRouter()
router.register(r'accounts', views.AccountViewSetV2)
router.register(r'wallets', views.WalletViewSet)
router.register(r'place', views.PlaceViewSet)
router.register(r'restaurant', views.RestaurantViewSet)

urlpatterns = router.urls
