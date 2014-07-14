from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from ca.models import UserProfile, Program, Package, Tracking
from ca.forms import UserProfileForm, UserForm

def home(request):
    context = RequestContext(request)
    return render_to_response('ca/home.html', context)


def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit = False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                print "Profile photo uploaded."
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
    return render_to_response('ca/profile.html', {'profile': profile, 'user': user}, context)

@login_required
def edit_profile(request):
    context = RequestContext(request)
    user = request.user
    if user.is_authenticated():
        profile = user.get_profile()

        if request.method == "POST":
            update_user_form = UserForm(request.POST, instance = user)
            update_profile_form = UserProfileForm(request.POST, instance = profile)
            if update_user_form.is_valid() and  update_profile_form.is_valid():
                user = update_user_form.save()
                user.set_password(user.password)
                profile = update_profile_form.save(commit = False)
                selected_fav_programs = update_profile_form.cleaned_data['fav_program']
                selected_packages = update_profile_form.cleaned_data['packages']
                # TODO: remove tracking for not_selected_packages
                # TODO: highlight packages, fav_programs that are already selected before
                profile.fav_program = selected_fav_programs
                # Manually save M2M through relationship
                for package in selected_packages:
                    tracking = Tracking.objects.get_or_create(package = package, user = profile)
                    print tracking
                    tracking[0].save()
                user.save()
                profile.save()
                print "Update profile successful"
                # Redirect to profile page
                return render_to_response("ca/profile.html", {
                    'user': user,
                    'profile': profile,
                    }, context)
        else:
            update_user_form = UserForm(instance = user)
            update_profile_form = UserProfileForm(instance = profile, initial = {'packages': [p.id for p in profile.packages.all()]})

        return render_to_response('ca/edit_profile.html', {
                    'profile': profile,
                    'user': user,
                    'programs': Program.objects.all(),
                    'packages': Package.objects.all(),
                    'edituser': update_user_form,
                    'editprofile': update_profile_form
                    },
                context)
    else:
        # TODO: Your session has timed out!
        pass 

# Helper function for program_search()
def search_program(max_program = 0, starts_with = {}):
    program_list = []
    if starts_with:
        filterargs = {}
        for k, v in starts_with.iteritems():
            if v:
                # Ignore case
                filterargs['{0}__{1}'.format(k, 'icontains')] = v

        if filterargs:
            program_list = Program.objects.filter(**filterargs)
        else:
            program_list = Program.objects.all()
    else:
        program_list = Program.objects.all()

    if max_program > 0:
        if len(program_list) > max_program:
            program_list = program_list[:max_program]

    return program_list

def program_search(request):
    context = RequestContext(request)
    starts_with = {}
    programs_list = []

    field_list = ['name']
    if request.method == "GET":
        for field in field_list:
            starts_with[field] = request.GET['search_' + field]
    else:
        for field in field_list:
            starts_with[field] = request.POST['search_' + field]

    program_list = search_program(10, starts_with)
    return render_to_response('ca/program_search.html', {'program_list': program_list}, context)
