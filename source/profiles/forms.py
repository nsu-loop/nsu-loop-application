from django import forms
from .models import Profile

class ProfileModelForm(forms.ModelForm):
    """
    This class contains the form of user profile.
    It holds the field names of user profile update form.
    """
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'bio', 'major', 'cgpa', 'email', 'phone', 'avatar')