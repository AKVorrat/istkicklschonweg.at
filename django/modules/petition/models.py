from django.db import models
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse
from urllib.parse import urlparse
from .tokens import TokenGenerator

generator = TokenGenerator()

class Signature(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    email = models.EmailField("E-Mail", max_length=255, unique=True)
    token = models.CharField(max_length=24, unique=True)
    emails_sent = models.IntegerField(default=0)

    confirmed = models.BooleanField(default=False)
    newsletter = models.BooleanField()

    class Meta:
        verbose_name = "Unterschrift"
        verbose_name_plural = "Unterschriften"

    def __str__(self):
        return '[{}] {} {}, {}'.format(
            'Confirmed' if self.confirmed else 'Pending',
            self.first_name, self.last_name, self.email 
        )
    
    def full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    def send_confirmation_email(self, request):
        if not self.token:
            self.token = generator.make_token(self)
        confirmation_url = '/confirm/{}/'.format(self.token)
        confirmation_url = request.build_absolute_uri(confirmation_url)
        send_mail(
            '[istkicklschonweg.at] Bitte bestätige deine E-Mail Adresse.',
            """Hallo {0},
            
            danke für deine Unterstützung unserer Forderung zum Rücktritt von Innenminister Herbert Kickl.
            Damit wir deine Stimme zählen können fehlt nur mehr ein kleiner Schritt!
            
            Bitte verwende diesen Bestätigungslink:
            
            {1}

            Vielen Dank für deine Hilfe!

            Liebe Grüße,
            xyz von epicenter.works""".format(self.full_name(), confirmation_url),
            'noreply@epicenter.works',
            [self.email],
            html_message=render_to_string(
                'email/confirm.html', 
                {
                    'confirmation_url': confirmation_url,
                    'full_name': self.full_name()
                }
            ),
            fail_silently=False
        )
        self.emails_sent += 1
        self.save()

    def confirm(self, token):
        if generator.check_token(self, token):
            self.confirmed = True
            self.save()

class Sin(models.Model):
    description = models.CharField(max_length=255)
    share_text = models.CharField(max_length=255)
    source_url = models.URLField()

    @property
    def source_host(self):
        url = urlparse(self.source_url)
        return url.netloc
