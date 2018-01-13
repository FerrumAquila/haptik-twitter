# App Imports
import serialisers
from twitter.resources import models


# Django Imports
from django.contrib.auth.models import User


class Profile(models.AetosModel):
    user = models.ForeignKey(User, related_name='profile')
    gender = models.CharField(max_length=2)
    dob = models.DateField(null=True, blank=True)

    class Options:
        create_serialiser = serialisers.CreateProfileSerialiser

    def __unicode__(self):
        return "%s '%s' %s" % (self.user.first_name, self.user.username, self.user.last_name)


class Tweet(models.AetosModel):
    author = models.ForeignKey(Profile, related_name='tweets')
    text = models.TextField(max_length=140)
    tags = models.ManyToManyField(Profile, related_name='tagged_in')

    class Options:
        create_serialiser = serialisers.CreateTweetSerialiser

    @classmethod
    def _save_object(cls, obj, data):
        obj.save()
        for tag in data.get('tags', list()):
            obj.tags.add(tag)
        obj.save()

    @property
    def data_json(self):
        return {'author': str(self.author), 'text': self.text, 'timestamp': self.created_at}


class Follow(models.AetosModel):
    follower = models.ForeignKey(Profile, related_name='followed')
    followed = models.ForeignKey(Profile, related_name='follower')

    class Options:
        create_serialiser = serialisers.CreateFollowSerialiser
