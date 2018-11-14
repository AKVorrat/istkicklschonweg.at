from django import forms, template
from .models import Signature

class SignatureForm(forms.ModelForm):
    auto_id = False
    first_name = forms.CharField(
        label="",
        max_length=256,
        widget=forms.TextInput(attrs={'placeholder': 'Vorname', 'class': "petition-input"})
    )
    last_name = forms.CharField(
        label="",
        max_length=256, 
        widget=forms.TextInput(attrs={'placeholder': 'Nachname', 'class': "petition-input"})
    )
    message = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={'placeholder': 'Message', 'class': "petition-input"})
    )

    email = forms.EmailField(
        label="",
        max_length=256, 
        widget=forms.TextInput(attrs={'placeholder': 'EMail', 'class': "petition-input"})
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
        fields = ['first_name', 'last_name', 'message', 'email', 'newsletter']
