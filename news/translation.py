from modeltranslation.translator import translator, register, TranslationOptions
from mezzanine.core.translation import TranslatedSlugged, TranslatedDisplayable, TranslatedRichText
from news.models import ListNews, News

@register(ListNews)
class ListNewsTranslationOptions(TranslationOptions):
    fields = ('titre_general',)

# @register(News)
# class NewsTranslationOptions(TranslationOptions):
#     fields = ('news_description',)

class TranslatedNews(TranslatedDisplayable):
    fields = ('title', 'news_description', 'resume', 'lieu', 'public_cible', )

translator.register(News, TranslatedNews)
