from django.contrib import admin
from django.urls import path, include
from .views import (
    ImageViewSet
)
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'images', ImageViewSet)
urlpatterns = [
    path('main/', include(router.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)