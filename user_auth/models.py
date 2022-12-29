from django.db import models
from enum import Enum


class UserTypesChoices(Enum):
    # A subclass of Enum
    admin = "admin"
    user = "user"


class User(models.Model):
    name = models.CharField(max_length=128, default=True, null=True, blank=True, )
    email = models.CharField(max_length=128, default=True, null=True, blank=True, )
    profile_image = models.ImageField(upload_to="profile/")
    email_verified_at = models.CharField(max_length=128, default=True, null=True, blank=True, )
    password = models.CharField(max_length=128, default=True, null=True, blank=True, )
    remember_token = models.CharField(max_length=128, default=True, null=True, blank=True, )
    user_type = models.CharField(max_length=128, default=True, null=True, blank=True,
                                 choices=[(tag, tag.value) for tag in UserTypesChoices])
    credit = models.CharField(max_length=128, default=True, null=True, blank=True, )

    class Meta:
        db_table = 'users'
    #     managed = False


class Notifications(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    notification = models.CharField(max_length=128, null=True, blank=True)
    is_seen = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
