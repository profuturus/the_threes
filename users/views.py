from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout

def logout_view(request):
    ''' log the user out '''
    logout(request)
    return HttpResponseRedirect(reverse('the_threes_tracker:index'))
