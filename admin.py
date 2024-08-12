from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, PostBox
# Register your models here.

# unregister groups
admin.site.unregister(Group)

# combine profiles w/ user
# !!!!Maybe will have to edit to allow non account holding users to user site!!!!!!


class profCombo(admin.StackedInline):
    model = Profile

# user stuff


class UserAdmin(admin.ModelAdmin):
    model = User
    # display user on admin page
    fields = ["username"]
    inlines = [profCombo]


# user/admin/profile management
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# user profile
admin.site.register(Profile)

# register post box
admin.site.register(PostBox)
