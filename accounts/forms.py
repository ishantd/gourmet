from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name')
        widgets = {
            'username': forms.EmailInput(attrs={
                'placeholder': 'Email',
            }),
            'email': forms.HiddenInput,
        }

    def save(self, commit=True):
        user = super().save(False)
        user.email = user.username
        user = super().save()

        return user
