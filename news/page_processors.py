from mezzanine.pages.page_processors import processor_for
from .models import ListNews, News

@processor_for(ListNews)
def news_list_function(request, page):
    news_list = News.objects.all()
    ctx = {'news_list' : news_list}
    return ctx
