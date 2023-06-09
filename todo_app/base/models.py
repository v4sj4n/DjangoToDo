from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_completed = models.BooleanField()

    def __str__(self) -> str:
        return f"{self.title}"
