# Django Imports
from django.dispatch import Signal

webhook_pinged = Signal(providing_args=['request_data'])


class BaseWebHook(object):

    SIGNAL = webhook_pinged

    @classmethod
    def _emit_signal(cls, data):
        cls.SIGNAL.send(sender=cls, request_data=data)

    @classmethod
    def _parse_request(cls, request):
        """
        extract data from request object
        :param request: django view request object
        :return: extracted request data from request object
        """
        raise NotImplementedError('Implement Request Parser')

    @classmethod
    def _process_data(cls, request_data):
        """
        implement request data serialisation
        :param request_data: json data from webhook request
        :return: serialised data
        """
        raise NotImplementedError('Implement Processing Data')

    @classmethod
    def process(cls, request):
        request_data = cls._parse_request(request)
        processed_data = cls._process_data(request_data)
        cls._emit_signal(processed_data)
        return processed_data
