from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import Group

def admin_perm(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.groups.filter(name='Admin').exists():
                return func(request, *args, **kwargs)

            raise PermissionDenied("Sizda bu amallarni bajarish huquqi yo'q.")

        return HttpResponse('403 Forbidden')

    return wrapper
