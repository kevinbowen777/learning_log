from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Topic(models.Model):
    """A topic the user is learning about."""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

    def get_absolute_url(self):
        return reverse("topic", args=[str(self.id)])


class Entry(models.Model):
    """Something specific learned about a topic."""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text[:]) < 50:
            return f"{self.text}"
        else:
            return f"{self.text[:50]}..."
