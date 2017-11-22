from mezzanine.pages.page_processors import processor_for
from .models import HomePage
from news.models import News, ListNews

@processor_for(HomePage)
def news_list_function(request, page):
    """Implicit: there is only one ListNews page."""
    listnews = ListNews.objects.first()
    max_news_on_homepage = listnews.max_news_domo
    news_list = News.objects.all()[0:max_news_on_homepage]
    ctx = {'news_list' : news_list}
    return ctx
