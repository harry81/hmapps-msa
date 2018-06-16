from __future__ import unicode_literals
from django.core.management.base import BaseCommand
import twitter
api = twitter.Api(consumer_key='TjrH7bAp3ClLhfo5yv5C19h6R',
                  consumer_secret='YNODKfpGN2OCYp6uRHYhXDuGI4EvhWnk8K9pOjwakGts0YsP9y',
                  access_token_key='574955920-IGfxVUhZm1ChKJxHgfiOrXzBwB0Nr81T9wjnQFGW',
                  access_token_secret='qToSq43eojIi9kb3LWlHR9iV2xwC9FaCToXLRDYUgcR9E')


class Command(BaseCommand):
    def handle(self, *args, **options):
        query = "q=ai&since=2017-10-10&count=100"
        geocode = [37.4974502, 127.0009563, "100km"]
        results = api.GetSearch(
            raw_query=query,
            geocode=geocode,
            result_type='popular',
            lang='ko')

        for status in results:
            print(status.user.screen_name, status.text, "\n")
