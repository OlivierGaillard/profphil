from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import RichText, Orderable, Slugged
from mezzanine.pages.models import Page
from mezzanine.forms.models import Form, FormEntry, FieldEntry, Field

"""
The table made by the whisiwig editor does not allow to customize the headers.
We need floating texts in place of links with titles, because the titles are not 
displayable on mobile or tablets.

The minimalistic goal is to have a normal page (not a richtext) like the homepage
within we can use the JQuery function to created the informational floating texts. 

A more elaborated version could be to mimic the news-list and news-items. The page table
would then list the table-rows like the news-list. Each row could have its fields with notes or
floating info. 

But would it be not simpler to build a form, retrieve the data and use them within the table?
The form can be made with Mezzanine form.  

TODO: see how to make a partial collectstatic.

"""

class PageTable(Page):
    canton_header = models.CharField(max_length=30, default="Canton")
    message = models.TextField(null=True, blank=True)
    os = models.CharField(max_length=10, null=True, blank=True, help_text="option spécifique")
    os_title = models.CharField("texte de la note pour OS", max_length=100, null=True, blank=True)
    oc = models.CharField(max_length=10, null=True, blank=True, help_text="option complémentaire")
    oc_title = models.CharField("texte de la note pour OC", max_length=100, null=True, blank=True)
    bmsh = models.CharField(max_length=10, null=True, blank=True, help_text="branche de matu")
    bmsh_title = models.CharField("texte de la note pour BMSH", max_length=100, null=True, blank=True)
    bm10 = models.CharField(max_length=10, null=True, blank=True, help_text="10e branche de matu")
    bm10_title = models.CharField("texte de la note pour BM10", max_length=100, null=True, blank=True)
    bc = models.CharField(max_length=10, null=True, blank=True, help_text="branche cantonale")
    bc_title = models.CharField("texte de la note pour BC", max_length=100, null=True, blank=True)
    cf = models.CharField(max_length=10, null=True, blank=True, help_text="cours facultatif")
    cf_title = models.CharField("texte de la note pour CF", max_length=100, null=True, blank=True)
    ev = models.CharField(max_length=10, null=True, blank=True, help_text="évaluation")
    ev_title = models.CharField("texte de la note pour EV", max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = _("Panorama")

class Canton(models.Model):
    nom = models.CharField(max_length=50)
    canton_OS =  models.NullBooleanField(null=True, blank=True)
    note_OS   = models.CharField(max_length=400, null=True, blank=True)
    symbole_note_OS = models.CharField(max_length=50, default="**", null=True, blank=True)
    OC = models.NullBooleanField(default=True, null=True, blank=True)
    note_OC = models.CharField(max_length=400, null=True, blank=True)
    symbole_note_OC = models.CharField(max_length=50, default="**", null=True, blank=True)
    BMSH = models.NullBooleanField(default=False, null=True, blank=True)
    note_BMSH = models.CharField(max_length=400, null=True, blank=True)
    symbole_note_BMSH = models.CharField(max_length=50, default="**", null=True, blank=True)
    BM10 = models.NullBooleanField(default=False, null=True, blank=True)
    note_BM10 = models.CharField(max_length=400, null=True, blank=True)
    symbole_note_BM10 = models.CharField(max_length=50, default="**", null=True, blank=True)
    BC   = models.NullBooleanField(default=False, null=True, blank=True)
    note_BC = models.CharField(max_length=400, null=True, blank=True)
    symbole_note_BC = models.CharField(max_length=50, default="**", null=True, blank=True)
    CF   = models.NullBooleanField(default=False, null=True, blank=True)
    note_CF = models.CharField(max_length=400, null=True, blank=True)
    symbole_note_CF = models.CharField(max_length=50, default="**", null=True, blank=True)
    EV   = models.CharField(max_length=400, null=True, blank=True)
    note_EV   = models.CharField(max_length=400, null=True, blank=True)
    symbole_note_EV = models.CharField(max_length=50, default="**", null=True, blank=True)

    def get_data_toogle(self):
        return '<a href="#" data-toggle="tooltip" title="%s">%s</a>'

    def get_note(self, option_code):
        option_dic = {'OS' : self.note_OS, 'OS_note' : self.symbole_note_OS,
                      'OC': self.note_OC, 'OC_note' : self.symbole_note_OC,
                      'BMSH' : self.note_BMSH, 'BMSH_note' : self.symbole_note_BMSH,
                      'BM10' : self.note_BM10, 'BM10_note' : self.symbole_note_BM10,
                      'BC' : self.note_BC, 'BC_note' : self.symbole_note_BC,
                      'CF' : self.note_CF, 'CF_note' : self.symbole_note_CF,
                      'EV' : self.note_EV, 'EV_note' : self.symbole_note_EV}
        if option_dic[option_code]:
            return self.get_data_toogle() % (option_dic[option_code], option_dic[option_code + '_note'])
        else:
            return ''

    @property
    def get_note_OS(self):
        return self.get_note('OS')

    @property
    def get_note_OC(self):
        return self.get_note('OC')

    @property
    def get_note_BMSH(self):
        return self.get_note('BMSH')

    @property
    def get_note_BM10(self):
        return self.get_note('BM10')

    @property
    def get_note_BC(self):
        return self.get_note('BC')

    @property
    def get_note_CF(self):
        return self.get_note('CF')

    @property
    def get_note_EV(self):
        return self.get_note('EV')

    class Meta:
        ordering = ['nom']

