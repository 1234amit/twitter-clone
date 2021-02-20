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
    
    """
    qs = Tweet.objects.all()
    tweets_list = [{"id":x.id, "content":x.content} for x in qs]
    data = {
        "response": tweets_list
    }

    return JsonResponse(data)
