from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from dabber.forms import RegistrationForm, LoginForm
from dabber.models import Dabber
from django.contrib.auth import authenticate, login, logout

def DabberRegistration(request):
        if request.user.is_authenticated():
                return HttpResponseRedirect('/profile/')
        if request.method == 'POST':
                form = RegistrationForm(request.POST)
                if form.is_valid():
                        user = User.objects.create_user(username=form.cleaned_data['username'], email = form.cleaned_data['email'], password = form.cleaned_data['password'])
                        user.save()
                        dabber = Dabber(user=user, name=form.cleaned_data['username'], birthday=form.cleaned_data['birthday'])
                        dabber.save()
			human = True
                        return HttpResponseRedirect('/profile/')
                else:   
                        return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))
        else:   
                ''' user is not submitting the form, show them a blank registration form '''
                form = RegistrationForm()
                context = {'form': form}
                return render_to_response('register.html', context, context_instance=RequestContext(request))

def LoginRequest(request):
        if request.user.is_authenticated():
                return HttpResponseRedirect('/profile/')
        if request.method == 'POST':
                form = LoginForm(request.POST)
                if form.is_valid():
                        username = form.cleaned_data['username']
                        password = form.cleaned_data['password']
                        dabber = authenticate(username=username, password=password)
                        if dabber is not None:
                                login(request, dabber)
                                return HttpResponseRedirect('/profile/')
                        else:   
                                return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
        else:   
                ''' user is not submitting the form, show the login form '''
                form = LoginForm()
                context = {'form': form}
                return render_to_response('login.html', context, context_instance=RequestContext(request))

def LogoutRequest(request):
        logout(request)
        return HttpResponseRedirect('/')

@login_required
def UserProfile(request):
        if not request.user.is_authenticated():
                return HttpResponseRedirect('/login/')
        dabber = request.user.profile.name
        birthday = request.user.profile.birthday
        email   = request.user.profile.email
	dbr_pic = request.user.profile.dbr_pic
        context = {'dabber': dabber}
        return render_to_response('profile.html', context, context_instance=RequestContext(request))

