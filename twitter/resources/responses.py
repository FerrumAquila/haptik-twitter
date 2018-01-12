# Django Imports
from django.http import JsonResponse

success = lambda m, d: JsonResponse(data={'success': 1, 'message': m, 'data': d})
failure = lambda e, d: JsonResponse(data={'success': 0, 'error': e, 'data': d})
