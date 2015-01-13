from django.shortcuts import render, render_to_response
from django.template import RequestContext
from pages.models import HomePage
from django.utils.html import urlize
from django.utils.safestring import mark_safe
import re

# Create your views here.

def MainHomePage(request):
        homepage = HomePage.objects.get(pk=1)
        context = {'homepage': homepage, 'tweets': getTweets()}
        return render_to_response('index.html', context, context_instance=RequestContext(request))

''' INTERNAL FUNCTION - not called from a URL '''
def getTweets():
        tweets = []
        try:
                import twitter
                api = twitter.Api(consumer_key='xxxxxxxxxxxxxx',
                      consumer_secret='xxxxxxxxxxxxxxxxxxxxxxxxxxx',
                      access_token_key='xxxxxxxxxxxxxxxxxxxxxxxxxx',
                      access_token_secret='xxxxxxxxxxxxxxxxxxxxxxxxx')

                latest = api.GetUserTimeline('dabfinder')
                for tweet in latest:
                        status = mark_safe(urlize(tweet.text))
                        myStatus = status
                #       r = re.compile(r"(http://[^ ]+)")
                        tweet_date = tweet.relative_created_at
                #       newstat = r.sub(r'<a href="\1">\1</a>', myStatus)
                        tweets.append({'status': status, 'date': tweet_date})
        except:
                tweets.append({'status': 'Follow us @dabfinder', 'date': 'about 10 minutes ago'})
        return {'tweets': tweets}



def Robots(request):
        return render_to_response('robots.txt')        
        

def Tou(request):
        return render_to_response('tou.html')

def Team(request):
        return render_to_response('team.html')

def Ad(request):
        return render_to_response('ad.html')

def Contact(request):
        return render_to_response('contact.html')
