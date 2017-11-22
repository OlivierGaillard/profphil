from mezzanine.pages.page_processors import processor_for
from .models import PageTable, Canton
from django.db.models import ObjectDoesNotExist


@processor_for(PageTable)
def cantons_list_function(request, page):
    # try:
    #     cantons_list = Canton.objects.all()
    #     ctx = {'cantons' : cantons_list}
    #     return ctx
    # except ObjectDoesNotExist:
    #     return {'cantons' : []}
    cantons_list = Canton.objects.all()
    ctx = {'cantons' : cantons_list}
    return ctx
