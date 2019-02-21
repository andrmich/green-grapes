from django.db import models
from django.urls import reverse
from django.utils.translation import gettext


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    # translations = TranslatedFields(
    # title = models.CharField(max_length=250)
#)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
