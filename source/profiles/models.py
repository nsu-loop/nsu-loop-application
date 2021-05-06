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
        """
        This method will return the absolute url of profile view.

        :param name: self - access the attributes
        :param type: reference
        :return: view
        """
        return reverse("profiles:profile-detail-view", kwargs={"slug": self.slug})

    initial_first_name = None
    initial_last_name = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial_first_name = self.first_name
        self.initial_last_name = self.last_name

    def save(self, *args, **kwargs):
        """
        This method will save the user profile details.

        :param name: self - access the attributes
        :param type: reference
        :param name: *args - pass number of arguments to a function
        :param type: variable
        :param name: **kwargs - pass key-value parameters to the function
        :param type: variable
        :return: Boolean
        """
        ex = False
        to_slug = self.slug
        if self.first_name != self.initial_first_name or self.last_name != self.initial_last_name or self.slug == "":
            if self.first_name and self.last_name:
                to_slug = slugify(str(self.first_name) + " " + str(self.last_name))
                ex = Profile.objects.filter(slug=to_slug).exists()
                while ex:
                    to_slug = slugify(to_slug + " " + str(get_random_code()))
                    ex = Profile.objects.filter(slug=to_slug).exists()
            else:
                to_slug = str(self.user)
        self.slug = to_slug
        super().save(*args, **kwargs)

    # def get_friends(self):
    #    return self.friends.all()

    # def get_friends_no(self):
    #  return self.friends.all().count()

    # def get_posts_no(self):
    #    return self.posts.all().count()

    # def get_all_authors_posts(self):
    #   return self.posts.all()

    # def get_likes_given_no(self):
    #  likes = self.like_set.all()
    # total_liked = 0
    # for item in likes:
    #    if item.value=='Like':
    #       total_liked += 1
    # return total_liked

    # def get_likes_recieved_no(self):
    #    posts = self.posts.all()
    #   total_liked = 0
    #  for item in posts:
    #     total_liked += item.liked.all().count()
    # return total_liked


class Skill(models.Model):
    """
    This class contains the fields and behaviour of the skill data type.
    It represents the database table fields.
    """
    name = models.CharField(max_length=15)

    def __str__(self):
        """
        This method will return skill name.

        :param name: self - access the attributes
        :param type: reference
        :return: str
        """
        return f"{self.name}"
