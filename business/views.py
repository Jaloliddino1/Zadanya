from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Phone
from .forms import PhoneForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.decorators import login_required, user_passes_test

def not_client(user):
    return not user.groups.filter(name='Client').exists()


def phone_list(request):
    q=request.GET.get('q')
    if q:
        phones = Phone.objects.filter(Q(name__icontains=q) | Q(brand__icontains=q))
    else:
        q=''
        phones = Phone.objects.all()
    is_admin = request.user.groups.filter(name='Admin').exists()
    return render(request, 'Phone/phone_list.html', {
        'phones': phones,
        'is_admin': is_admin,
        'q':q
    })

@login_required
@permission_required('business.can_publish_phone', raise_exception=True)
def phone_create(request):
    form = PhoneForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('business:phone_list')
    return render(request, 'Phone/phone_form.html', {'form': form})
@login_required
@permission_required('business.can_publish_phone', raise_exception=True)
def phone_update(request, id):
    phone = get_object_or_404(Phone, id=id)
    form = PhoneForm(request.POST or None, instance=phone)
    if form.is_valid():
        form.save()
        return redirect('business:phone_list')
    return render(request, 'Phone/phone_form.html', {'form': form})
@login_required
@permission_required('business.can_publish_phone', raise_exception=True)
def phone_delete(request, id):
    phone = get_object_or_404(Phone, id=id)
    if request.method == 'POST':
        phone.delete()
        return redirect('business:phone_list')
    return render(request, 'Phone/phone_confirm_delete.html', {'phone': phone})
from django.contrib.auth.decorators import permission_required

@permission_required('business.can_publish_phone', raise_exception=True)
def publish_phone(request, phone_id):
    phone = get_object_or_404(Phone, id=phone_id)
    phone.published = True
    phone.save()
    return redirect('business:phone_list')


def file_upload(request):
    if request.method == 'POST':
        form= PhoneForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('business:file_list')
        return render(request,'file/file_upload.html',{'form':form})
    form = PhoneForm()
    return render(request,'file/file_upload.html',{'form':form})


def file_list(request):
    files=Phone.objects.all()

    return render(request,'file/file_list.html',{'files': files})