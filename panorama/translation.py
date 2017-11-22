from modeltranslation.translator import translator, register, TranslationOptions
from mezzanine.core.translation import TranslatedSlugged, TranslatedDisplayable, TranslatedRichText
from .models import PageTable, Canton



@register(PageTable)
class PageTableTranslationOptions(TranslationOptions):
    fields = ('canton_header', 'message', 'os', 'oc', 'bmsh', 'bm10', 'bc', 'cf', 'ev',
              'os_title', 'oc_title', 'bmsh_title', 'bm10_title', 'bc_title', 'cf_title', 'ev_title')


@register(Canton)
class TranslatedCanton(TranslationOptions):
    fields = ( 'nom',
               'note_OS',
               'note_OC',
               'note_BMSH',
               'note_BM10',
               'note_BC',
               'note_CF',
               'EV', 'note_EV', )

