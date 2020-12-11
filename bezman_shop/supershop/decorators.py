from django.shortcuts import redirect


def allowed_roles(allowed=[]):
    def decorator(function):
        def wrap(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed:
                return function(request, *args, **kwargs)
            else:
                return redirect('products')
        return wrap
    return decorator


