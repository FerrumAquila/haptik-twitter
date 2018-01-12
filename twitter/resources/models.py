# Package Imports
from model_utils.models import TimeStampedModel

# Django Imports
from django.db.models import *


class AetosModel(TimeStampedModel):
    """
    from resources import models

    class YourModel(models.AetosModel):
        your_column = models.CharField
        class Options:
            create_serialiser = SerialiserClass
    """
    is_active = BooleanField(default=True)
    active = BooleanField(default=True)
    created_at = DateTimeField(auto_now_add=True)
    modified_at = DateTimeField(auto_now=True)
    extra_data = TextField(default='{}')

    class Meta:
        abstract = True

    class Options:
        create_serialiser = None

    @classmethod
    def _save_object(cls, obj, data):
        obj.save()

    @classmethod
    def create_from_serialiser(cls, data, serialiser_class=None):
        if not hasattr(serialiser_class, 'required_json'):
            serialiser_class = None
            if not cls.Options.create_serialiser:
                raise Exception('Missing Default Serialiser')

        serialiser = serialiser_class or cls.Options.create_serialiser
        obj = cls(**serialiser(data).required_json)
        cls._save_object(obj, data)
        return obj
