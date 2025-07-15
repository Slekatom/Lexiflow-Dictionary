from django.urls import path
from .views import *

urlpatterns = [
    path("", DictionariesListView.as_view(), name = "dictionaries"),
]