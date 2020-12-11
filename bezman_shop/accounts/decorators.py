from django.http import HttpResponse
from django.shortcuts import redirect

def admin_only(function):
    def wrap(request, *args, **kwargs):
            if request.user.is_staff:
                return function(request, *args, **kwargs)
            else:
                return HttpResponse("{'data':'you have no permission!'}")
    return wrap

