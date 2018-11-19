from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import SignatureForm
from .models import Signature

class PetitionView(FormView):
    template_name = 'index.html'
    form_class = SignatureForm
    success_url = '/thanks/'

    def form_valid(self, form, request):
        res = super(FormView, self).form_valid(form)
        form.instance.send_confirmation_email(request)
        return res
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        for field in form:
            print(field)
            print(type(field))
        if form.is_valid():
            return self.form_valid(form, request)
        else:
            return self.form_invalid(form)
            
class ConfirmEmailView(TemplateView):
    template_name = 'confirm.html'

    def get(self, request, *args, token=None, **kwargs):
        try:
            signature = Signature.objects.get(token=token)
        except Signature.DoesNotExist:
            return super().get(request, *args, confirmed=False, **kwargs)
        signature.confirm(token)
        return super().get(request, *args, confirmed=signature.confirmed, **kwargs)
