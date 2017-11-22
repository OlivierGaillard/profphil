from django.contrib import admin
from mezzanine.pages.admin import PageAdmin, DisplayableAdmin

from .models import HomePage
# Register your models here.

admin.site.register(HomePage, PageAdmin)