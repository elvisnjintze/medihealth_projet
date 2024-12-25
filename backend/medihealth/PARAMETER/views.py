from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import CMPPAR
from .serializers import CMPPARSerializer


class CMPPARList(ModelViewSet):
    serializer_class = CMPPARSerializer

    def get_queryset(self):
        return CMPPAR.objects.all()

