from django.conf import settings
from django.views.static import serve
from django.conf.urls import url, include
from django.contrib import admin
from modules.petition.views import PetitionView, ConfirmEmailView, \
    PrivacyView, ConfirmWithdrawalView
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^confirm/(?P<token>.{24})/', ConfirmEmailView.as_view(), name="confirm-email"),
    url(r'^thanks/$', TemplateView.as_view(template_name="thanks.html")),
    url(r'^privacy/$', PrivacyView.as_view()),
    url(r'^privacy/withdrawal$', TemplateView.as_view(template_name="withdrawal_sent.html")),
    url(r'^withdraw/(?P<token>.{24})/', ConfirmWithdrawalView.as_view()),
    url(r'^\/?$', PetitionView.as_view())
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', serve, {
            'document_root': settings.STATIC_ROOT,
        }),
    ]
