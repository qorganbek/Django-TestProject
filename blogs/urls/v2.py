from django.urls import path, include
from blogs import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'blogs', views.BlogView)

urlpatterns = router.urls
