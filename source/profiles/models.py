from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.shortcuts import reverse
from django.template.defaultfilters import slugify

from .utils import get_random_code


class Profile(models.Model):
    """
    This class contains the fields and behaviour of the profile data type.
    It represents the database table fields.
    """
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="no bio...", max_length=300)
    email = models.EmailField(max_length=200, blank=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    major = models.CharField(max_length=200, blank=True, null=True)
    cgpa = models.FloatField(blank=True, null=True)
    grad_year = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=200, blank=True)
    avatar = models.ImageField(default='avatar.png', upload_to='avatars/')
    friends = models.ManyToManyField(User, blank=True, related_name='friends')
    skills = models.JSONField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        This method will return username and created time.

        :param name: self - access the attributes
        :param type: reference
        :return: str
        """
        return f"{self.user.username}-{self.created.strftime('%d-%m-%Y')}"

    def get_absolute_url(self):
        return reverse("profiles:profile-detail-view", kwargs={"slug": self.slug})
