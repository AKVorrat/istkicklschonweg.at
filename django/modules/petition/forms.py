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
        try:
            s = Signature.objects.get(email=email)
        except:
            return
        if not s.confirmed:
            if s.emails_sent < 5:
                self.pending_signature = s
                self.add_error('email', 'Eine unbestätigte Unterschrift mit dieser E-Mail-Adresse existiert bereits. Wir haben die Bestätigungsanfrage erneut versandt.')
            else:
                self.add_error('email', 'Eine unbestätigte Unterschrift mit dieser E-Mail-Adresse existiert bereits und es wurden insgesamt bereits fünf Bestätigungsanfragen versandt.')

    class Meta:
        auto_id = False
        model = Signature
        fields = ['first_name', 'last_name', 'email', 'newsletter']
