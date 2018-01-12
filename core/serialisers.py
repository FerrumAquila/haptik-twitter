# App Imports
from twitter.resources.serialisers import *


class CreateProfileSerialiser(Serializer):
    BODY_MAP = {
        'user': ('user', as_is),
        'gender': ('gender', as_is),
        'dob': ('dob', datetime_from_timestamp),
    }
    REDUCER = dict_reducer


class CreateTweetSerialiser(Serializer):
    BODY_MAP = {
        'author': ('author', as_is),
        'text': ('text', as_is),
    }
    REDUCER = dict_reducer


class CreateFollowSerialiser(Serializer):
    BODY_MAP = {
        'follower': ('follower', as_is),
        'followed': ('followed', as_is),
    }
    REDUCER = dict_reducer

