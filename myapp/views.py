from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required

# def home(request):
#     return redirect(reverse('home'))

def home(request):
    if (request.user.is_authenticated()):
        return render(request, 'myapp/home.html')
    return login(request, template_name='myapp/home.html')


@login_required
def profile(request):
    return render(request, template_name='myapp/profile.html')
 