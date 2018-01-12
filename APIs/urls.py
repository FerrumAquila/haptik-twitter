# App Imports
import views

# Django Imports
from django.conf.urls import url


urlpatterns = [
    # GET
    url(r'^profile/(?P<profile_id>[0-9]+)/dashboard-tweets/$', views.dashboard_tweets, name='dashboard_tweets'),

    # POST
    url(r'^profile/new/$', views.create_user_profile, name='create_user_profile'),
    url(r'^tweet/new/$', views.publish_tweet, name='publish_tweet'),
    url(r'^profile/(?P<follower_id>[0-9]+)/follow/(?P<followed_id>[0-9]+)/$', views.add_follow, name='add_follow'),
]
