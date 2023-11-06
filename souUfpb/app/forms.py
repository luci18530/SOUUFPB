from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):

    email = forms.EmailField()
    
    class Meta:
        model = User  # Substitua por seu modelo de usuário, se necessário
        fields = ('username', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalize os campos do formulário, se necessário
        self.fields['username'].label = 'Nome de usuário'
        self.fields['email'].label = 'E-mail'
        self.fields['password1'].label = 'Senha'
        self.fields['password2'].label = 'Confirme a senha'


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalize os campos do formulário, se necessário
        self.fields['username'].label = 'Nome de usuário'
        self.fields['password'].label = 'Senha'