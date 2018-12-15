from django import forms, template
from django.utils.safestring import mark_safe
from .models import Signature

class SignatureForm(forms.ModelForm):
    auto_id = False
    required_css_class = 'required'
    first_name = forms.CharField(
        label="Vorname",
        max_length=255,
        widget=forms.TextInput(attrs={'class': "petition-input"})
    )
    last_name = forms.CharField(
        label="Nachname",
        max_length=255,
        widget=forms.TextInput(attrs={'class': "petition-input"})
    )

    email = forms.EmailField(
        label="E-Mail Adresse",
        max_length=255,
        widget=forms.TextInput(attrs={'class': "petition-input"})
    )

    newsletter = forms.BooleanField(
        initial=False,
        required=False,
        label=mark_safe('Ich will den <a target="_blank" href="https://epicenter.works/newsletter">Newsletter</a> erhalten.')
    )
    privacy_policy = forms.BooleanField(
        initial=False,
        required=True,
        label=mark_safe('Ich stimme den <a target="_blank" href="/privacy">Datenschutzbedingungen</a> zu.')
    )

    def clean(self):
        super(SignatureForm, self).clean()
        email = self.cleaned_data.get('email')
        self.pending_signature = None
        self.confirmed_signature = None
        try:
            s = Signature.objects.get(email=email)
        except Signature.DoesNotExist:
            return

        if not s.confirmed:
            self.pending_signature = s
        else:
            self.confirmed_signature = s

    class Meta:
        auto_id = False
        model = Signature
        fields = ['first_name', 'last_name', 'email', 'newsletter']

class WithdrawalForm(forms.Form):
    email = forms.EmailField(
        label="E-Mail-Adresse",
        max_length=255,
        widget=forms.TextInput(attrs={'class': "petition-input"})
    )

    def clean(self):
        super(WithdrawalForm, self).clean()
        email = self.cleaned_data.get('email')
        self.signature = None
        try:
            self.signature = Signature.objects.get(email=email)
        except Signature.DoesNotExist:
            return
        if self.signature.withdrawal_emails_sent >= 5:
            self.signature = None
