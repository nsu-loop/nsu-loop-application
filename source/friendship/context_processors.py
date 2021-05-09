from .models import Profile, Relationship








def profile_pic(request):

    '''
    This method will pass the avatar of requested user profile
    after authenticating the user .
    :param name: request - it generates the response(HTTP)
    :param type: HttpResponse
    :return: returns a response

    '''
    if request.user.is_authenticated:
        profile_obj = Profile.objects.get(user=request.user)
        pic = profile_obj.avatar
        return {'picture':pic}
    return {}



def invatations_received_no(request):

    '''
    This method will count the number of invitation received after
    authenticating the user request  
    :param name: request - it generates the response(HTTP)
    :param type: HttpResponse
    :return: int

    '''
    if request.user.is_authenticated:
        profile_obj = Profile.objects.get(user=request.user)
        qs_count = Relationship.objects.invatations_received(profile_obj).count()
        return {'invites_num':qs_count}
    return {}