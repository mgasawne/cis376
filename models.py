from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class PostBox(models.Model):
    user = models.ForeignKey(User, related_name="posts",
                             on_delete=models.CASCADE)
    header = models.CharField(max_length=255, default='')  # Header field
    body = models.TextField(default='')  # Body field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.header} by {self.user} ({self.created_at:%Y-%m-%d %H:%M})"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField("self",
                                     related_name="followed_by",
                                     symmetrical=False,
                                     blank=True)
    date_modified = models.DateTimeField(
        auto_now=True)  # corrected `auto_now` parameter

    def __str__(self):
        return self.user.username


def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()


class Comment(models.Model):
    post = models.ForeignKey(
        PostBox, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.header}'


post_save.connect(create_profile, sender=User)
