from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

#posts/not repos. Could change to make into repo? can likely reuse code for comments too
class postBox(models.model):
    user = models.ForeignKey(
        User, related_name="posts",
        on_delete=models.NONE
    )

    #post length/will have to change to fit reqs
    body = models.CharField(max_Length = 300)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return(
            f"{self.user} "
            f"({self.created_at :%Y-%m-%d %H:%M}): "
            f"{self.body}..."
        )

# Create your models here. Will need to create account/non-account holder user here
class Profile(models.Model):
    #when user is deleted, everything gets deleted
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    #allows users to follow other users/not sure if we need it tho
    follows = models.ManyToManyField("self", 
                                     related_name = "followed_by",
                                     symmetrical = False,
                                     blank = True)
    date_modified = models.DateTimeField(User, auto_now = True)

    def __str__(self):
        return self.user.username

#combo user w/ profile
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user = instance)
        user_profile.save()

post_save.connect(create_profile, sender = User)

    