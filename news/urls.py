from django.conf.urls import url
from .views import news_detail

app_name = 'news'

urlpatterns = [
    url(r'news_detail/(?P<pk>[0-9]+)$', news_detail, name='news_detail'),
]