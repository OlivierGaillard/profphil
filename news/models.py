from django.shortcuts import reverse
from django.db import models
from mezzanine.pages.models import Page, Link
from mezzanine.core.models import Displayable, Ownable, RichText, RichTextField

class ListNews(Page):
    titre_general = models.CharField(max_length=200)
    max_news_domo = models.SmallIntegerField("Nbre maximum de news sur 'Domo'", default=8, null=True, blank=True)

class News(Displayable):
    lieu   = models.CharField(max_length=200, null=True, blank=True)
    date_debut = models.DateField(null=True, blank=True)
    heure_debut = models.TimeField(null=True, blank=True)
    date_fin   = models.DateField(null=True, blank=True)
    heure_fin = models.TimeField(null=True, blank=True)
    public_cible = models.CharField(max_length=150, null=True, blank=True)
    resume = RichTextField(max_length=800, null=True, blank=True)
    news_description = RichTextField("Détails", null=True, blank=True)
    edit_date = models.DateTimeField(auto_now=True)
    edit_date_label = models.CharField(max_length=100, default="Ajouté le" , null=True, blank=True)


    def get_absolute_url(self):
        return reverse('news:news_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-edit_date']
        verbose_name_plural = 'News'


