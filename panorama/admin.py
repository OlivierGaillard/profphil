from django.contrib import admin
from mezzanine.pages.admin import PageAdmin, DisplayableAdmin

from .models import PageTable, Canton
# Register your models here.

admin.site.register(PageTable, PageAdmin)


class CantonAdmin(admin.ModelAdmin):
    list_display = ('nom', 'canton_OS', 'OC', 'BMSH', 'BM10', 'BC', 'CF', 'EV' )

admin.site.register(Canton, CantonAdmin)
# Register your models here.
