from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import resolve
from .forms import SignUpForm, CompanyFORM
from django.contrib import messages
from administration.models import Theme,Profile, education, license_certification, skills_selection, Project,Company_profile
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.

## Changing the m=in built django authentication system
class UsernameEmailAuthBackend(ModelBackend):
    """Username or Email login"""

    def authenticate(self, request, username=None, password=None, **kwargs):
        """Determine whether the username (Email) and password are correct"""
        query_set = User.objects.filter( Q(username=username) |  Q(email=username))
        try:
            if query_set.exists():
                user = query_set.get()
                if user.check_password(password):
                    return user
        except:
            return None
        return None
    
def theme_custom(request):
    if Theme.objects.filter(user=request.user).exists():
        color = Theme.objects.get(user=request.user).color
    else:
        color = 'light'
    
    return color 

@login_required(login_url="login")
def home(request):
    theme = theme_custom(request)
    return render(request, 'home.html', {'color':theme})

@login_required(login_url="login")
def profile(request):
    theme = theme_custom(request)
    profiles_about = Profile.objects.select_related("user_name").get(user_name=request.user).about
    profiles_industry = Profile.objects.select_related("user_name").get(user_name=request.user).industry
    profiles_country = Profile.objects.select_related("user_name").get(user_name=request.user).country
    profiles_city = Profile.objects.select_related("user_name").get(user_name=request.user).city
    profiles_linkedin_url = Profile.objects.select_related("user_name").get(user_name=request.user).linkedin_url
    profiles_github_url = Profile.objects.select_related("user_name").get(user_name=request.user).github_url
    profiles_website_url = Profile.objects.select_related("user_name").get(user_name=request.user).website_url
    profiles_address = Profile.objects.select_related("user_name").get(user_name=request.user).address
    profiles_birthday = Profile.objects.select_related("user_name").get(user_name=request.user).birthday

    projects = Project.objects.filter(user_name = request.user)
    licensing = license_certification.objects.filter(user_name = request.user)
    educations = education.objects.filter(user_name = request.user)
    skills = skills_selection.objects.filter(user_name = request.user)

    return render(request, 'profile/profile.html', {
        'profiles_about':profiles_about, 'profiles_industry':profiles_industry, 'profiles_country':profiles_country,
        'profiles_city':profiles_city,'profiles_linkedin_url':profiles_linkedin_url,'profiles_github_url':profiles_github_url,
        'profiles_website_url':profiles_website_url,'profiles_address':profiles_address,'profiles_birthday':profiles_birthday,

        'project':projects,'license':licensing,'edu':educations, 'skillsets':skills,'color':theme,
    })

@login_required(login_url="login")
def create_user(request):
    theme = theme_custom(request)
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            form.save()
            messages.success(request, 'Your account has been created!')
            return redirect('register')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration.html', {'form': form,'color':theme})

@login_required(login_url="login")
def view_company(request):
    current_url = resolve(request.path_info).url_name
    theme = theme_custom(request)
    all_companies = Company_profile.objects.all()
    form = CompanyFORM(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'The company has been created!')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        
    context = {
        'companies': all_companies,
        'color':theme,
        'form':form,
    }
    return render(request, 'company/view_company.html', context)

def theme(request):
    color = request.GET.get('color')
    current_url = resolve(request.path_info).url_name
    # previous_url = self.request.META.get('HTTP_REFERER')
    if color == 'dark':
        if Theme.objects.filter(user=request.user).exists():
            user_theme = Theme.objects.get(user=request.user)
            user_theme.user = request.user
            user_theme.color = 'dark'
            user_theme.save()
        else:
            user2 = Theme(user=request.user, color='dark')
            user2.save()

    elif color == 'light':
        if Theme.objects.filter(user=request.user).exists():
            user_theme1 = Theme.objects.get(user=request.user)
            user_theme1.user = request.user
            user_theme1.color = 'light'
            user_theme1.save()
        else:
            user4 = Theme(user=request.user, color='light')
            user4.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def error_404(request, exception):
    data = {}
    return render(request,'error_pages/error_404.html', data)

def error_500(request):
        data = {}
        return render(request,'error_pages/error_500.html', data)