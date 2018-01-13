# App Imports
import models

# Django Imports
from django.shortcuts import render_to_response

# from IPython.frontend.terminal.embed import InteractiveShellEmbed
# InteractiveShellEmbed()()


def home(request):
    profile = models.Profile.objects.filter(user=request.user).first()
    return render_to_response('core/home.html', {'profile_id': profile.pk})
