from django.contrib import admin

from .models import Beneficiary, PR_Request

admin.site.register(Beneficiary)
admin.site.register(PR_Request)
