from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from .models import Dictionary
from .forms import DictionaryCreate

class DictionariesListView(ListView):
    model = Dictionary
    template_name = "dictionary/dictionary_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dicts = Dictionary.objects.filter(user = self.request.user)
        context["user_dictionaries"] = dicts
        return context


class DictionaryCreateView(CreateView):
    model = Dictionary
    form_class = DictionaryCreate
    template_name = "dictionary/dictionary_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        dictionary = form.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("dictionary:dict")

class DictionaryUpdateView(UpdateView):
    model = Dictionary
    template_name = "dictionary/dictionary_update.html"
    fields = ["language1", "language2", "notice"]

    def form_valid(self, form):
        responce = super().form_valid(form)
        return responce

    def get_success_url(self):
        return reverse_lazy("dictionary:dict")





