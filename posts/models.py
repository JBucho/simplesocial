from django.db import models
from django.urls import reverse
from django.conf import settings
from groups.models import Group

import misaka

from django.contrib.auth import get_user_model
User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name='posts',
                              null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:single',
                        kwargs={
                            'username':self.user.username,
                            'pk':self.pk
                            }
                      )

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'message']


class Comment(models.Model):
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    text = models.TextField()
    text_html = models.TextField(editable=False)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    approved_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        self.text_html = misaka.html(self.text)
        super().save(*args, **kwargs)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('posts:single',
                        kwargs={
                            'username':Post.user.username,
                            'pk':self.post.pk
                            }
                      )
