from django.http import HttpResponse
from functools import wraps


class RoleChoices:
    Admin = 'Admin'
    Client = 'Client'

def admin_perm(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.groups.filter(name=RoleChoices.Admin).exists():
                return func(request, *args, **kwargs)
            return HttpResponse('403 Forbidden: Sizda bu amalni bajarishga ruxsat yo‘q.', status=403)
        return HttpResponse('401 Unauthorized: Iltimos, avval login qiling.', status=401)
    return wrapper

