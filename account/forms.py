from django import forms
from .models import User
from django.contrib.auth.forms import PasswordResetForm, UserCreationForm,PasswordChangeForm,SetPasswordForm

# from . models import Register
#class SignupForm(UserCreationForm):
#    class Meta(UserCreationForm.Meta):
#        model = get_user_model()
#        fields = ("username", "email", "first_name", "last_name", "role")



class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields=['username','email','password1','password2']

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'] = forms.CharField(max_length=50, required=True)
        self.fields['email'] = forms.EmailField(max_length=50, required=True)


        self.fields[ 'password1' ] = forms.CharField(
            strip=False,
            widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
            help_text='veuillez taper un mot de passe',
        )
        self.fields[ 'password2' ] = forms.CharField(
            strip=False,
            widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
            help_text='veuillez retaper un mot de passe',
        )


class UserLoginForm(forms.Form):
    username = forms.CharField(label="Nom  d'utilisateur", widget=forms.TextInput(
        attrs={'placeholder': "Entrer votre nom d'utilisateur", 'id': 'user'}), max_length=50, required=True)
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput(
        attrs={'placeholder': 'Entrer votre mot de passe', 'id': 'pwd'}), max_length=50, min_length=6, required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']