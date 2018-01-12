# App Imports
import utils
from twitter.resources import responses
from core import models as core_models

# Django Imports
from django.views.decorators.csrf import csrf_exempt

# Package Imports
import json

# from IPython.frontend.terminal.embed import InteractiveShellEmbed
# InteractiveShellEmbed()()


@csrf_exempt
def create_user_profile(request):
    user_id = 1
    request_data = json.loads(request.body)
    request_data.update({'user': core_models.User.objects.get(pk=user_id)})

    # request_data = {'user': core_models.User.objects.all().first(), 'gender': 'M', 'dob': 663680993}
    try:
        profile = core_models.Profile.create_from_serialiser(request_data)
    except Exception:
        profile = None

    if profile:
        return responses.success('profile %s created' % str(profile), {
            'profile_id': profile.id, 'user_id': profile.user.id
        })
    else:
        return responses.failure('profile not created', {'user_id': user_id})


@csrf_exempt
def publish_tweet(request):
    request_data = json.loads(request.body)
    request_data.update({'author': core_models.Profile.objects.get(pk=request_data['author'])})
    if 'tags' in request_data:
        request_data.update({'tags': core_models.Profile.objects.filter(pk__in=request_data['tags'])})

    # request_data = {'author': core_models.Profile.objects.all().first(), 'text': 'shell tweet',
    #                 'tags': list(core_models.Profile.objects.all()[1:])}
    try:
        tweet = core_models.Tweet.create_from_serialiser(request_data)
    except Exception:
        tweet = None

    if tweet:
        return responses.success('tweet %s created' % str(tweet), {
            'tweet_id': tweet.id, 'author': str(tweet.author)
        })
    else:
        return responses.failure('tweet not created', dict())


@csrf_exempt
def add_follow(request, follower_id, followed_id):
    follower = core_models.Profile.objects.get(pk=follower_id)
    followed = core_models.Profile.objects.get(pk=followed_id)

    try:
        follow = core_models.Follow.create_from_serialiser({'follower': follower, 'followed': followed})
    except Exception:
        follow = None

    if follow:
        return responses.success('follow %s created' % str(follow), {
            'follow_id': follow.id, 'follower': str(follow.follower), 'followed': str(follow.followed)
        })
    else:
        return responses.failure('follow not created', dict())


@csrf_exempt
def dashboard_tweets(request, profile_id):
    profile = core_models.Profile.objects.get(pk=profile_id)

    tweets = utils.ProfileHandler(profile).get_dashboard_tweets()

    if tweets:
        return responses.success('tweets for %s found' % str(profile), {
            'tweets': [t.data_json for t in tweets], 'profile_id': profile.id
        })
    else:
        return responses.failure('tweets for %s not found' % str(profile), dict())
