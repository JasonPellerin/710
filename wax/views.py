from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from wax.models import Wax, Dispensary
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from dabber.models import Dabber
from django.contrib.auth import authenticate, login, logout
from django.utils.html import urlize
from django.utils.safestring import mark_safe
from wax.forms import *

# Create your views here.

def WaxsAll(request):
        waxs = Wax.objects.all().order_by('name')
        context = {'waxs': waxs }
        return render_to_response('waxsall.html', context,  context_instance=RequestContext(request))

def DispensarysAll(request):
        dispensarys 	= Dispensary.objects.all().order_by('name')
        context 	= {'dispensarys': dispensarys }
        return render_to_response('dispensarysall.html', context, context_instance=RequestContext(request))

def SpecificWax(request, waxslug):
        wax 	= Wax.objects.get(slug=waxslug)
        context = { 'wax': wax }
        return render_to_response('singlewax.html', context, context_instance=RequestContext(request))

def SpecificDispensary(request, dispensaryslug):
        dispensary 	= Dispensary.objects.get(slug=dispensaryslug)
        waxs 		= Wax.objects.filter(dispensary=dispensary)
        context 	= {'waxs': waxs }
        return render_to_response('singledispensary.html', context, context_instance=RequestContext(request))




@login_required
def UserProfile(request):
        if not request.user.is_authenticated():
                return HttpResponseRedirect('/login/')
        dabber 		= request.user.profile.name
        birthday 	= request.user.profile.birthday
        email   	= request.user.profile.email
	dbr_pic 	= request.user.profile.dbr_pic
        context 	= {'dabber': dabber}
        return render_to_response('waxsall.html', context, context_instance=RequestContext(request))
