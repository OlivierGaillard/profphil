from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin, DisplayableAdmin
from .models import ListNews, News, Membres

admin.site.register(ListNews, PageAdmin)

news_fieldsets = deepcopy(DisplayableAdmin.fieldsets)
news_fieldsets[0][1]["fields"].insert(-2, "resume")
news_fieldsets[0][1]["fields"].insert(-2, "news_description")
news_fieldsets[0][1]["fields"].insert(-2, "lieu")
news_fieldsets[0][1]["fields"].insert(-2, "date_debut")
news_fieldsets[0][1]["fields"].insert(-2, "heure_debut")
news_fieldsets[0][1]["fields"].insert(-2, "date_fin")
news_fieldsets[0][1]["fields"].insert(-2, "heure_fin")
news_fieldsets[0][1]["fields"].insert(-2, "public_cible")

class NewsAdmin(DisplayableAdmin):
    fieldsets = news_fieldsets

admin.site.register(News, NewsAdmin)

class MembresAdmin(admin.ModelAdmin):
    list_display = ('vorname', 'nachname')

admin.site.register(Membres, MembresAdmin)
