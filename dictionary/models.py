from django.contrib.auth.models import User
from django.db import models
import choices as c
from django.core.exceptions import ValidationError

class Dictionary(models.Model):
    LANGUAGE_CHOICES = c.languages()
    language1 = models.CharField(max_length=50, choices=LANGUAGE_CHOICES)
    language2 = models.CharField(max_length=50, choices=LANGUAGE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    notice = models.TextField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dictionaries")

    def clean(self):
        if self.language1 == self.language2:
            raise ValidationError("The original language cannot be identical to the translation language.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user}'s {self.language1}-{self.language2} dictionary"

class Topic(models.Model):
    title = models.CharField(max_length=50, default="default")
    created_at = models.DateTimeField(auto_now_add=True)
    level = models.CharField(max_length=50, choices=c.levels())
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="topics")

    def __str__(self):
        return f"{self.user}'s Topic: {self.title}"

class Word(models.Model):
    word = models.CharField(max_length=100, default="None")
    translation = models.CharField(max_length=100, default="None")
    created_at = models.DateTimeField(auto_now_add=True)
    pronunciation = models.CharField(max_length=100, blank=True, null=True)
    example = models.TextField(max_length=200, null=True, blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="words")
    part_of_speech = models.CharField(max_length=100, choices=c.parts_of_speech())


    def clean(self):
        if self.word == self.translation:
            raise ValidationError("The word cannot be identical to its translation")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.word}-{self.translation}"




