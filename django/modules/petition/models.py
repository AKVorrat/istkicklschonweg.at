from django.db import models
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse
from .tokens import TokenGenerator

generator = TokenGenerator()

class Signature(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    message = models.TextField()

    email = models.EmailField(max_length=256, unique=True)
    token = models.CharField(max_length=20, unique=True)

    confirmed = models.BooleanField(default=False)
    newsletter = models.BooleanField()

    def __str__(self):
        return '[{}] {} {}, {}'.format(
            'Confirmed' if self.confirmed else 'Pending',
            self.first_name, self.last_name, self.email 
        )

    def send_confirmation_email(self, request):
        self.token = generator.make_token(self)
        self.save()
        confirmation_url = '/confirm/{}/'.format(self.token)
        confirmation_url = request.build_absolute_uri(confirmation_url)
        send_mail(
            'Bitte bestätige deine E-Mail Adresse.',
            '',
            'noreply@epicenter.works',
            [self.email],
            html_message=render_to_string('email/confirm.html', {'confirmation_url': confirmation_url}),
            fail_silently=False
        )

    def confirm(self, token):
        if generator.check_token(self, token):
            self.confirmed = True
            self.save()
