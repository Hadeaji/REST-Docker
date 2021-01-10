from django.contrib import admin
from django.urls import path, include

from .views import Engine_1ListView,Engine_1DetailsView

urlpatterns = [
    path('',Engine_1ListView.as_view(),name= 'engines'),
    path('<int:pk>/',Engine_1DetailsView.as_view(),name = 'offer_details'),
]