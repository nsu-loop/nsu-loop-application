from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.db.models import Q

# Create models here.
class Profile(models.Model):
    """
    This class contains the essential fields and behaviors of the data you’re storing. 
    Each model maps to a single database table.
    
    This class is used to create a database table containg those attributes.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='avatar.png', upload_to='avatars/')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
		This method will return user's username and creation time.

		:param name: self - used to access the attributes and methods of the class in python
		:param type: reference
		:return: str
		"""
        return f"{self.user.username}-{self.created.strftime('%d-%m-%Y')}"



