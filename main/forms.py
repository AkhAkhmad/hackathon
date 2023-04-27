from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

CHECKOUT = (
    ("athletes", "Спортсмен"),
    ("federation_partner", "Партнер Федерации"),
    ("fsp_administrator", "Администратор ФСП"),
    ("representative_of_the_regional_federation", "Представитель Региональной Федерации"),
)


class RegisterForm(UserCreationForm):
    choice = forms.ChoiceField(choices=CHECKOUT)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'choice')
