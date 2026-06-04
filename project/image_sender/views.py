from django.shortcuts import render
from rest_framework import viewsets
from .models import Image
from .serializers import ImageSerializer
# Create your views here.
class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer