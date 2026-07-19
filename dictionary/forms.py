from django.forms import forms, ModelForm
from .models import Dictionary, Topic


class DictionaryCreate(ModelForm):
    class Meta:
        model = Dictionary
        fields = ["language1", "language2", "notice"]

class TopicCreate(ModelForm):
    class Meta:
        model = Topic
        fields = ["title", "level"]