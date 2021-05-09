from django.shortcuts import render
from .models import Relationship
from .forms import ProfileModelForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



@login_required
def invites_received_view(request):
    """ 
    This function will redirect the my_invites page.If profile = request user then add the profile in invite list.

    :param name: request - it generates the response(HTTP)
    :param type: HttpResponse
    :return: returns a signal

    """
    profile = Profile.objects.get(user=request.user)
    qs = Relationship.objects.invatations_received(profile)
    results = list(map(lambda x: x.sender, qs))
    is_empty = False
    if len(results) == 0:
        is_empty = True

    context = {
        'qs': results,
        'is_empty': is_empty,
    }

    return render(request, 'profiles/my_invites.html', context)



@login_required
def accept_invatation(request):
    """

    This function will redirect the URL of my-invites-view.
    This function will save the sender and receiver profile if the status is accepted.
    
    :param name: request - it generates the response(HTTP)
    :param type: HttpResponse
    :return: returns an URL
    
    """
    if request.method=="POST":
        pk = request.POST.get('profile_pk')
        sender = Profile.objects.get(pk=pk)
        receiver = Profile.objects.get(user=request.user)
        rel = get_object_or_404(Relationship, sender=sender, receiver=receiver)
        if rel.status == 'send':
            rel.status = 'accepted'
            rel.save()
    return redirect('profiles:my-invites-view')



@login_required
def reject_invatation(request):

    """ 
    This function will redirect the URL of my-invites-view if the status is rejected.

    :param name: request - it generates the response(HTTP)
    :param type: HttpResponse
    :return: returns an URL

    """
    if request.method=="POST":
        pk = request.POST.get('profile_pk')
        receiver = Profile.objects.get(user=request.user)
        sender = Profile.objects.get(pk=pk)
        rel = get_object_or_404(Relationship, sender=sender, receiver=receiver)
        rel.delete()
    return redirect('profiles:my-invites-view')


# This function will redirect the profile_list page.
# If user = request user then will add it to profile_list.  
@login_required
def profiles_list_view(request):
    """ 
    This function will redirect the profile_list page.
    If user = request user then will add it to profile_list.

    :param name: request - it generates the response(HTTP)
    :param type: HttpResponse
    :return: returns an URL

    """


    user = request.user
    qs = Profile.objects.get_all_profiles(user)

    context = {'qs': qs}

    return render(request, 'profiles/profile_list.html', context)

# Class based view. 

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profiles/detail.html'


# This method functionality is pass the sender and user profile in the database through context.

    def get_context_data(self, **kwargs):
        """
        This method functionality is pass the sender and user profile in the database through context.

        :param name: self - used to access the attributes and methods of the class in python
        :param type: reference
        :param name: **kwargs - used to pass key-value parameters to the function
        :param type: pass variable
        :return: str
        """
        context = super().get_context_data(**kwargs)
        user = User.objects.get(username__iexact=self.request.user)
        profile = Profile.objects.get(user=user)
        rel_r = Relationship.objects.filter(sender=profile)
        rel_s = Relationship.objects.filter(receiver=profile)
        rel_receiver = []
        rel_sender = []
        for item in rel_r:
            rel_receiver.append(item.receiver.user)
        for item in rel_s:
            rel_sender.append(item.sender.user)
        context["rel_receiver"] = rel_receiver
        context["rel_sender"] = rel_sender
        context['posts'] = self.get_object().get_all_authors_posts()
        context['len_posts'] = True if len(self.get_object().get_all_authors_posts()) > 0 else False
        return context

#class based view

class ProfileListView(LoginRequiredMixin, ListView):
    """
    class based view. 

    """
    model = Profile
    template_name = 'profiles/profile_list.html'
    # context_object_name = 'qs'



    def get_queryset(self):
        """
        this method will set pass the quertset in   the database.

        :param name: self - used to access the attributes and methods of the class in python
        :param type: reference
        :return: query set

        """



        qs = Profile.objects.get_all_profiles(self.request.user)
        return qs

    def get_context_data(self, **kwargs):
        """
        This method functionality is pass the sender and user profile in the database through context.

        :param name: self - used to access the attributes and methods of the class in python
        :param type: reference
        :param name: **kwargs - used to pass key-value parameters to the function
        :param type: pass variable
        :return: str
        """
        context = super().get_context_data(**kwargs)
        user = User.objects.get(username__iexact=self.request.user)
        profile = Profile.objects.get(user=user)
        rel_r = Relationship.objects.filter(sender=profile)
        rel_s = Relationship.objects.filter(receiver=profile)
        rel_receiver = []
        rel_sender = []
        for item in rel_r:
            rel_receiver.append(item.receiver.user)
        for item in rel_s:
            rel_sender.append(item.sender.user)
        context["rel_receiver"] = rel_receiver
        context["rel_sender"] = rel_sender
        context['is_empty'] = False
        if len(self.get_queryset()) == 0:
            context['is_empty'] = True

        return context

# this function will redirect the url of my-profile-view when a request will be sent.

@login_required
def send_invatation(request):
    """ 
    This function will redirect the url of my-profile-view when a request will be sent. 

    :param name: request - it generates the response(HTTP)
    :param type: HttpResponse
    :return: returns an URL

    """
    if request.method=='POST':
        pk = request.POST.get('profile_pk')
        user = request.user
        sender = Profile.objects.get(user=user)
        receiver = Profile.objects.get(pk=pk)

        rel = Relationship.objects.create(sender=sender, receiver=receiver, status='send')

        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('profiles:my-profile-view')

# This func will redirect the url of my-profile-view when a friend will be removed.
    
@login_required
def remove_from_friends(request):
    """ 
    This func will redirect the url of my-profile-view when a friend will be removed. 

    :param name: request - it generates the response(HTTP)
    :param type: HttpResponse
    :return: returns an URL

    """
    if request.method=='POST':
        pk = request.POST.get('profile_pk')
        user = request.user
        sender = Profile.objects.get(user=user)
        receiver = Profile.objects.get(pk=pk)

        rel = Relationship.objects.get(
            (Q(sender=sender) & Q(receiver=receiver)) | (Q(sender=receiver) & Q(receiver=sender))
        )
        rel.delete()
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('profiles:my-profile-view')