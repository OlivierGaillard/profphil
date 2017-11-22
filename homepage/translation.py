from modeltranslation.translator import translator, register, TranslationOptions
from mezzanine.core.translation import TranslatedSlugged, TranslatedDisplayable, TranslatedRichText
from .models import HomePage

@register(HomePage)
class HomePageTranslationOptions(TranslationOptions):
    fields = ('titre_dernieres_nouvelles', 'message_de_bienvenue', 'content', )