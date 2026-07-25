from django.urls import path
from .views import *

app_name = "dictionary"

urlpatterns = [
    path("", DictionariesListView.as_view(), name = "dict"),
    path("create/", DictionaryCreateView.as_view(), name = "dict_create"),
    path("update/<int:pk>/", DictionaryUpdateView.as_view(), name = "dict_update"),
    path("delete/<int:pk>/", DictionaryDeleteView.as_view(), name = "dict_delete"),
    path("<int:pk>/", DictionaryDetailView.as_view(), name = "dict_detail"),
    path("<int:pk>/topic/create/", TopicCreateView.as_view(), name = "topic_create"),
    path("topic/delete/<int:pk>/", TopicDeleteView.as_view(), name = "topic_delete"),
]