from multiprocessing import context

from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Dictionary, Topic
from .forms import DictionaryCreate, TopicCreate


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

class DictionaryDeleteView(DeleteView):
    model = Dictionary
    template_name = "dictionary/dictionary_del.html"

    def get_success_url(self):
        return reverse_lazy("dictionary:dict")

class DictionaryDetailView(DetailView):
    model = Dictionary
    template_name = "dictionary/dictionary_detail.html"

    def get_context_data(self, **kwargs):
        dictionary = self.get_object()
        context = super().get_context_data(**kwargs)
        context["dictionary"] = dictionary
        return context

class TopicCreateView(CreateView):
    model = Topic
    form_class = TopicCreate
    template_name = "dictionary/topic_create.html"

    def form_valid(self, form):
        self.dictionary = get_object_or_404(
            Dictionary,
            pk=self.kwargs["pk"]
        )
        form.instance.user = self.request.user
        form.instance.dictionary = self.dictionary

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("dictionary:dict_detail", kwargs={"pk": self.dictionary.pk})

class TopicDeleteView(DeleteView):
    model = Topic
    template_name = "dictionary/topic_del.html"

    def get_success_url(self):
        return reverse(
            "dictionary:dict_detail",
            kwargs={"pk": self.object.dictionary.pk},
        )


