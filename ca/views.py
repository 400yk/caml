from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from ca.models import UserProfile
from ca.forms import UserProfileForm, UserForm

def home(request):
    context = RequestContext(request)
    return render_to_response('ca/home.html', context)

def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit = False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render_to_response('ca/register.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered,
        }, context)

def user_login(request):
    context = RequestContext(request)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            if user.is_active:
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user)
                return HttpResponseRedirect('/ca/')
            else:
                return HttpResponse('Your account has been disabled')
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid user name or password.")
    else:
        return render_to_response('ca/login.html', context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/ca/')

@login_required
def profile(request):
    context = RequestContext(request)
    user = request.user
    profile = UserProfile.objects.get(user = user)
    return render_to_response('ca/profile.html', {'profile': profile}, context)
