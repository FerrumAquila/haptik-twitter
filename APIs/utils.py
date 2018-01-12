# App Imports
from core import models as core_models


class ProfileHandler(object):

    def __init__(self, profile):
        self.instance = profile

    @property
    def all_following(self):
        return core_models.Follow.objects.filter(follower=self.instance).values_list('followed', flat=True)

    def get_dashboard_tweets(self):
        return core_models.Tweet.objects.filter(author__in=self.all_following)
