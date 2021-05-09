from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.db.models import Q


class ProfileManager(models.Manager):
    """
    This class contains the essential fields and behaviors of the data of an 
    individual profile  we’re storing in the database . Each model maps to
    a single database table.This class is used to create a database table 
    containg those attributes.

    """

    def get_all_profiles_to_invite(self, sender):

      '''
      This  method will add a user if accepted then their name will be stored and
      if a user is not accepted then their list will be again available 
      for accepting ,this will also exclude own user profile in the list 
      The query will fetch all accepted user  from the  objects and add
      user and the accpeted profile in a relationship after checking their status
      and will  show the list of users not accepted.

      :param name: self - used to access the attributes and methods of the class in python
      :param type: reference
      :param name: sender - the person who sends the invitation
      :param type: string
      :return: a status

      '''


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

# defines one  sent to databse and other parameter will be  to see in the browser
 
STATUS_CHOICES = (

    ('send', 'send'),
    ('accepted', 'accepted')
)

    
class RelationshipManager(models.Manager):

  ''' 
  This class contains the essential fields and behaviors of the data we’re storing
  for building the connection between two users in database ,when accepted a request .
  Each model maps to a single database table.
  This class is used to create a database table containg those attributes.

  '''

    def invatations_received(self, receiver):


      '''
      this method is used to receive  send request from the sender to the user 
      in the database 
      :param name: self - used to access the attributes and methods of the class in python
      :param type: reference
      :param name: receiver - the person who accepts the invitation
      :param type: reference
      :return: a query

      '''

      qs = Relationship.objects.filter(receiver=receiver, status='send')
        return qs


class Relationship(models.Model):

    '''
    This class is used  for building the essential fields and models for building the  relationship between the sender and the receiver, for connecting their interaction such as if one gets deleted
    other gets deleted automatically , if one user request is accepted  ,the acceptor's  friend count and sender's friend counts also gets updated .

    '''

    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = RelationshipManager()

    def __str__(self):

      """
      This method will return user's username and time it user was created
      :param name: self - used to access the attributes and methods of the class in python
      :param type: reference
      :return: str
        
      """
        return f"{self.sender}-{self.receiver}-{self.status}"