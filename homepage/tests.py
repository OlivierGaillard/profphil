from django.test import TestCase
from news.models import News
from django.utils import timezone
from mezzanine.core.models import CONTENT_STATUS_DRAFT, CONTENT_STATUS_PUBLISHED
import datetime

class LastNewsTest(TestCase):
    """Test the display of the news in the homepage.
    publish_date and expiry_date are fields inherited from 'Displayable'.
    """


    def test_news_expiry_date_in_the_future(self):
        t1 = timezone.make_aware(timezone.datetime(2017, 11, 23))
        t2 = timezone.make_aware(timezone.datetime(2017, 11, 24))
        news_1 = News(publish_date=t1, status=CONTENT_STATUS_PUBLISHED, expiry_date=t2)

        self.assertIsNotNone(news_1)
        news_1.save()
        homepage_list = News.objects.published()
        self.assertTrue(len(homepage_list) > 0)

    def test_news_expiry_date_is_today(self):
        t1 = timezone.make_aware(timezone.datetime(2017, 11, 22))
        t2 = timezone.make_aware(timezone.datetime(2017, 11, 23))
        news_1 = News(publish_date=t1, status=CONTENT_STATUS_PUBLISHED, expiry_date=t2)

        self.assertIsNotNone(news_1)
        news_1.save()
        homepage_list = News.objects.published()
        self.assertTrue(len(homepage_list) == 0)

