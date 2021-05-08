from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.db.models import Q


class ProfileManager(models.Manager):
"""
    This class contains the essential fields and behaviors of the data we’re storing. 
    Each model maps to a single database table.
    
    This class is used to create a database table containg those attributes.
    """

    def get_all_profiles_to_invite(self, sender):
        profiles = Profile.objects.all().exclude(user=sender)
        profile = Profile.objects.get(user=sender)
        qs = Relationship.objects.filter(Q(sender=profile) | Q(receiver=profile))
        print(qs)
        print("#########")

        accepted = set([])
        for rel in qs:
            if rel.status == 'accepted':
                accepted.add(rel.receiver)
                accepted.add(rel.sender)
        print(accepted)
        print("#########")

        available = [profile for profile in profiles if profile not in accepted]
        print(available)
        print("#########")
        return available
        

    def get_all_profiles(self, me):
        profiles = Profile.objects.all().exclude(user=me)
        return profiles

'''these functions defines one will be sent to databse and other parameter will be for us to
 see in the browser'''
STATUS_CHOICES = (
    ('send', 'send'),
    ('accepted', 'accepted')
)

class RelationshipManager(models.Manager):
   ''' This class contains the essential fields and behaviors of the data you’re storing. 
        Each model maps to a single database table.
    
        This class is used to create a database table containg those attributes.'''

    def invatations_received(self, receiver):
        qs = Relationship.objects.filter(receiver=receiver, status='send')
        return qs


class Relationship(models.Model):

   '''This class contains the essential fields and behaviors of the data you’re storing. 
      Each model maps to a single database table.
     
      This class is used to create a database table containg those attributes.'''

    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = RelationshipManager()

    def __str__(self):
      '''  """
  This method will return user's username and time it user was created
  :param name: self - used to access the attributes and methods of the class in python
  :param type: reference
  :return: str
        
  """'''
        return f"{self.sender}-{self.receiver}-{self.status}"