from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ObjectsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()[:500]


class Post(models.Model):
    objects = ObjectsManager()
    title = models.CharField()
    content = models.TextField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Follow(models.Model):
    objects = models.Manager()
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='follower')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='following')

    class Meta:
        unique_together = ('user', 'author')

