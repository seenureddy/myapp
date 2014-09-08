from django.core.urlresolvers import reverse
from django.shortcuts import redirect

def home(request):
    return redirect(reverse('home'))