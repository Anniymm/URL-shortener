from django.db import models
import string
import random

class URL(models.Model):
    original_url = models.URLField(max_length=200)
    short_url = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return f'{self.original_url} -> {self.short_url}'

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = self.generate_short_url()
        super().save(*args, **kwargs)

    def generate_short_url(self):
        characters = string.ascii_letters + string.digits
        short_url = ''.join(random.choice(characters) for _ in range(6))
        while URL.objects.filter(short_url=short_url).exists():
            short_url = ''.join(random.choice(characters) for _ in range(6))
        return short_url
