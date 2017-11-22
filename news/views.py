from django.shortcuts import render, get_object_or_404
from .models import News

def news_detail(request, pk):
    """ Display one news.
    """
    template = "news/news_detail.html"
    one_news = get_object_or_404(News, pk=pk)
    ctx = {"one_news": one_news}
    return render(request, template_name=template, context=ctx)
