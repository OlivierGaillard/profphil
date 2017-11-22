from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import RichText, Orderable, Slugged
from mezzanine.pages.models import Page
from mezzanine.utils.models import upload_to

class HomePage(Page, RichText):
    message_de_bienvenue = RichTextField(default="Bienvenue!")
    content = RichTextField(default="Corps du texte")
    titre_dernieres_nouvelles = models.CharField(max_length=200, default="Nouveautés récentes")

    class Meta:
        verbose_name = _("Page d'accueil")
        verbose_name_plural = _("Pages d'accueil")


