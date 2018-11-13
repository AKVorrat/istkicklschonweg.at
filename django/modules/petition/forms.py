from django import forms
from .models import Signature

class SignatureForm(forms.ModelForm):
    privacy_policy = forms.BooleanField(required = True)
    class Meta:
        model = Signature
        fields = ['first_name', 'last_name', 'message', 'email', 'newsletter']
