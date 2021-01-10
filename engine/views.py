from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView ,RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView

from .serializer import Engine_1Serializer
from .models import Engine_1
# Create your views here.

class Engine_1ListView(ListAPIView):
    queryset = Engine_1.objects.all()
    serializer_class = Engine_1Serializer

class Engine_1DetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Engine_1.objects.all()
    serializer_class = Engine_1Serializer