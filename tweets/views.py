import random
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from .models import Tweet
from .forms import TweetForm
# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, 'tweets/home.html', context={})

def tweet_create_view(request, *args, **kwargs):
    form = TweetForm()
    if request.method == 'POST':
        form = TweetForm(data=request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return HttpResponseRedirect(reverse('tweets:home'))
            form = TweetForm()
    return render(request, 'components/forms.html', context={'form':form, 'title':'tweet create view'})

def tweet_list_view(request, *args, **kwargs):
    """
    REST API VIEW
    Consume by javascript or Swift/java/ios/android
    return json data
    tweet_list_view
    """
    qs = Tweet.objects.all()
    tweets_list = [x.serialize() for x in qs]
    data = {
        "is_user":False,
        "response": tweets_list
    }

    return JsonResponse(data)
