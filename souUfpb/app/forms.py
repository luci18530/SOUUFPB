from django import forms
from .models import Choice
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class QuestionarioForm(forms.Form):
    def __init__(self, *args, **kwargs):
        perguntas = kwargs.pop('perguntas')
        super(QuestionarioForm, self).__init__(*args, **kwargs)
        
        for question in perguntas:
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                label=question.question_text,
                choices=Choice._meta.get_field('choice').choices
            )

class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalize os campos do formulário, se necessário
        self.fields['username'].label = 'Nome de usuário'
        self.fields['password1'].label = 'Senha'
        self.fields['password2'].label = 'Confirme a senha'

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalize os campos do formulário, se necessário
        self.fields['username'].label = 'Nome de usuário'
        self.fields['password'].label = 'Senha'