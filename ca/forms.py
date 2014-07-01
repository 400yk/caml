from django import forms
from ca.models import UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(help_text = "Password")
    username = forms.CharField(help_text = "Username")
    email = forms.CharField(help_text = "Email")
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        widgets = {
                'password': forms.PasswordInput(),
                }

class UserProfileForm(forms.ModelForm):
    picture = forms.ImageField(help_text = "Select an image", required = False)
    class Meta:
        model = UserProfile
        fields = ['phone', 'picture', 'skype_id', 'qq_id']
