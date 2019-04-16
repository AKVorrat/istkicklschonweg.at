from django.contrib import admin
from .models import Signature, Sin

class SignatureAdmin(admin.ModelAdmin):
    pass

class SinAdmin(admin.ModelAdmin):
    pass

admin.site.register(Signature, SignatureAdmin)
admin.site.register(Sin, SinAdmin)
