# Package Imports
import requests


class URLCleaner(object):
    URL_FORMAT_MAP = {
        '/path/': {
            'processes': [{
                'func': '_add_slash',
                'params': {'location': 'front'}
            }, {
                'func': '_add_slash',
                'params': {'location': 'back'}
            }]
        },
        '/path': {
            'processes': [{
                'func': '_add_slash',
                'params': {'location': 'front'}
            }, {
                'func': '_remove_slash',
                'params': {'location': 'back'}
            }]
        },
        'path/': {
            'processes': [{
                'func': '_remove_slash',
                'params': {'location': 'front'}
            }, {
                'func': '_add_slash',
                'params': {'location': 'back'}
            }]
        },
        'path': {
            'processes': []
        }
    }

    @classmethod
    def _add_slash(cls, url, location):
        if location == 'front':
            if not url.startswith('/'):
                return '/' + url
        if location == 'back':
            if not url.endswith('/'):
                return url + '/'
        return url

    @classmethod
    def _remove_slash(cls, url, location):
        if location == 'front':
            if url.startswith('/'):
                return url[1:]
        if location == 'back':
            if url.endswith('/'):
                return url[:-1]
        return url

    @classmethod
    def clean_url(cls, url, url_format):
        cleaned_url = url
        processes = cls.URL_FORMAT_MAP[url_format]['processes']
        for process in processes:
            cleaned_url = getattr(cls, process['func'])(cleaned_url, process['params']['location'])
        return cleaned_url


class Coordinator(URLCleaner):
    BASE_URL = ''

    @classmethod
    def _get_base_url(cls):
        cleaned_base = cls.clean_url(cls.BASE_URL, 'path/')
        return cleaned_base

    @classmethod
    def _get_path(cls, path):
        cleaned_path = cls.clean_url(path, 'path/')
        return cleaned_path

    @classmethod
    def _request_url(cls, path):
        return cls._get_base_url() + cls._get_path(path)

    @classmethod
    def get(cls, path, data):
        url = cls._request_url(path)
        requests.get(url=url, data=data)

    @classmethod
    def post(cls, path, data):
        url = cls._request_url(path)
        requests.post(url=url, json=data)
