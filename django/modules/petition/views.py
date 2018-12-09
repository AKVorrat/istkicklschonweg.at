from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import SignatureForm, WithdrawalForm
from .models import Signature, Sin

class PetitionView(FormView):
    template_name = 'index.html'
    form_class = SignatureForm
    success_url = '/thanks/'

    def get_context_data(self, **kwargs):
        kwargs['signature_count'] = Signature.objects.filter(confirmed=True).count()
        kwargs['sins'] = Sin.objects.all()
        return super(PetitionView, self).get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.instance.send_confirmation_email(request)
        else:
            if form.pending_signature:
                if form.pending_signature.emails_sent < 5:
                    form.pending_signature.send_confirmation_email(request)
            elif form.confirmed_signature:
                if form.confirmed_signature.emails_sent < 5:
                    form.confirmed_signature.send_already_confirmed_email(request)
            else:
                return self.form_invalid(form)
        return self.form_valid(form)
            
class ConfirmEmailView(TemplateView):
    template_name = 'confirm.html'

    def get(self, request, *args, token=None, **kwargs):
        try:
            signature = Signature.objects.get(token=token)
        except Signature.DoesNotExist:
            return super().get(request, *args, confirmed=False, **kwargs)
        signature.confirm(token)
        return super().get(request, *args, confirmed=signature.confirmed, **kwargs)

class PrivacyView(FormView):
    template_name = 'privacy.html'
    form_class = WithdrawalForm
    success_url = '/privacy/withdrawal'
    fail_url = '/privacy/#withdrawal'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            if form.signature:
                form.signature.send_withdrawal_email(request)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class ConfirmWithdrawalView(TemplateView):
    template_name = 'withdraw.html'

    def get(self, request, *args, token=None, **kwargs):
        try:
            signature = Signature.objects.get(withdrawal_token=token)
        except Signature.DoesNotExist:
            return super().get(request, *args, withdrawn=False, **kwargs)
        signature.withdraw(token)
        return super().get(request, *args, withdrawn=True, **kwargs)

