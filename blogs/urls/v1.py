from django.urls import path, include
from rest_framework import routers
from blogs import views

router = routers.DefaultRouter()
router.register(r'blogs', views.BlogView)

urlpatterns = router.urls
