# App Imports
import views

# Django Imports
from django.conf.urls import url


urlpatterns = [
    # HTML
    url(r'^home/$', views.home, name='core_home'),
    # url(r'^login/$', views.login, name='core_login'),
]
