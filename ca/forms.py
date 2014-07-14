from django import forms
from ca.models import UserProfile, Program, University, Package
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(help_text = "Password", widget = forms.PasswordInput)
    password_con = forms.CharField(help_text = "Confirm password", widget = forms.PasswordInput)
    username = forms.CharField(help_text = "Username")
    email = forms.CharField(help_text = "Email")

    def clean_password_con(self):
        pw1 = self.cleaned_data.get('password')
        pw2 = self.cleaned_data.get('password_con')
        if pw1 and pw1 != pw2:
            raise forms.ValidationError("Passwords don't match")
        return pw2

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    picture = forms.ImageField(help_text = "Select an image", required = False)
    fav_program = forms.ModelMultipleChoiceField(queryset = Program.objects.all(), to_field_name = "name", required = False)
    fav_university = forms.ModelMultipleChoiceField(queryset = University.objects.all(), required = False)
    packages = forms.ModelMultipleChoiceField(queryset = Package.objects.all(), required = False)
    class Meta:
        model = UserProfile
        fields = ['phone', 'picture', 'skype_id', 'qq_id', 'fav_program', 'fav_university', 'packages']


class EditUserForm(forms.ModelForm):
    password = forms.CharField(help_text = "Password")
    username = forms.CharField(help_text = "Username")
    email = forms.CharField(help_text = "Email")
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

class EditProfileForm(forms.ModelForm):
    username = forms.CharField(required = True)
    email = forms.EmailField(required = True)
    class Meta:
        model = UserProfile
        fields = ['phone', 'picture', 'skype_id', 'qq_id']
