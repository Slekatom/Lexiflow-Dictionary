from django.urls import path
from .views import *

app_name = "dictionary"

urlpatterns = [
    path("", DictionariesListView.as_view(), name = "dict"),
    path("create/", DictionaryCreateView.as_view(), name = "dict_create"),
    path("update/<int:pk>/", DictionaryUpdateView.as_view(), name = "dict_update"),
]