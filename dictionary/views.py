from django.shortcuts import render
from django.views.generic import ListView
from .models import Dictionary


class DictionariesListView(ListView):
    model = Dictionary
    template_name = "dictionary/dictionary_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dicts = Dictionary.objects.filter(user = self.request.user)
        context["user_dictionaries"] = dicts
        return context

