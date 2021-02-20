import random
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from .models import Tweet
# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, 'pages/home.html', context={})


def tweet_list_view(request, *args, **kwargs):
    """
    REST API VIEW
    Consume by javascript or Swift/java/ios/android
    return json data
    tweet_list_view
    """
    qs = Tweet.objects.all()
    tweets_list = [{"id":x.id, "content":x.content, "likes":random.randint(0, 129) } for x in qs]
    data = {
        "is_user":False,
        "response": tweets_list
    }

    return JsonResponse(data)
