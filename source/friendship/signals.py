from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Relationship

@receiver(post_save, sender=User)
'''
 this method will create a user profile
 :param name: post_save - used to send signals to profile model to create a profile
 :return: object
 '''
def post_save_create_profile(sender, instance, created, **kwargs):
    ''' this method will create a user profile
    :param name: sender - The model class that just had an instance created
    :param name: **kwargs -A dictionary of keyword arguments passed to __init__()
    :param type: variable
    :param name: created -A boolean; True if a new record was created.
    :param type: boolean
    :return: boolean
     '''
    
    if created:
        Profile.objects.create(user=instance)




@receiver(post_save, sender=Relationship)
def post_save_add_to_friends(sender, instance, created, **kwargs):
    '''
    this mehod will add two user in a relationship and will set up the conection between them
    with the help of signals i.e if an invitatio is accepted them both 
    users prfile will be added to each and friend count will be updated 
     
    :param name: sender - The model class that just had an instance created
    :param type: reference
    :param name: **kwargs -A dictionary of keyword arguments passed to __init__()
    :param type: variable
    :param name: created -A boolean; True if a new record was created.
    :param type:boolean
    :return: boolean


    '''
    sender_ = instance.sender
    receiver_ = instance.receiver
    if instance.status == 'accepted':
        sender_.friends.add(receiver_.user)
        receiver_.friends.add(sender_.user)
        sender_.save()
        receiver_.save()


@receiver(pre_delete, sender=Relationship)
def pre_delete_remove_from_friends(sender, instance, **kwargs):

    '''
     this mehod will remove  two user in a relationship and will break  the conection between them
    with the help of signals i.e if an invitation is rejected or a friend is unfriended them both 
    users prfile will be updated to each and friend count will decrease . 
     
    :param name: sender - The model class that just had an instance created

    :param name: **kwargs -A dictionary of keyword arguments passed to __init__()
    :param type: variable
    :param name: created -A boolean; True if a new record was created
    :param type: variable 
   

    :return: boolean

    '''
    sender = instance.sender
    receiver = instance.receiver
    sender.friends.remove(receiver.user)
    receiver.friends.remove(sender.user)
    sender.save()
    receiver.save()