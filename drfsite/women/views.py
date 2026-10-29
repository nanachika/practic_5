from django.shortcuts import render
from rest_framework import generics
from .models import Women
from .serializers import WomenSerializer
from rest_framework.permissions import AllowAny

class WomenAPIView(generics.ListAPIView):
    queryset = Women.objects.all().order_by('id')
    serializer_class = WomenSerializer
    permission_classes = [AllowAny]
    pagination_class = None
# Create your views here.
