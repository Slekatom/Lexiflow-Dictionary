from django.forms import forms, ModelForm
from .models import Dictionary


class DictionaryCreate(ModelForm):
    class Meta:
        model = Dictionary
        fields = ["language1", "language2", "notice"]
