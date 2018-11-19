from django import forms, template
from .models import Signature

class SignatureForm(forms.ModelForm):
    auto_id = False
    required_css_class = 'required'
    first_name = forms.CharField(
        label="Vorname",
        max_length=256,
        widget=forms.TextInput(attrs={'placeholder': '', 'class': "petition-input"})
    )
    last_name = forms.CharField(
        label="Nachname",
        max_length=256, 
        widget=forms.TextInput(attrs={'placeholder': '', 'class': "petition-input"})
    )

    email = forms.EmailField(
        label="E-Mail Adresse",
        max_length=256, 
        widget=forms.TextInput(attrs={'placeholder': '', 'class': "petition-input"})
    )

    newsletter = forms.BooleanField(
        initial=False,
        required=False,
        label="Ich will den Newsletter erhalten."
    )
    privacy_policy = forms.BooleanField(
        initial=False,
        required=True,
        label="Ich stimme der Privacy Policy zu."
    )

    class Meta:
        auto_id = False
        model = Signature
        fields = ['first_name', 'last_name', 'email', 'newsletter']
