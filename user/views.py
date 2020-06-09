"""A parser for HTML and XHTML."""

# This file is based on sgml
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from home.models import UserProfile
from product.models import Product
from user.forms import UserUpdateForm, ProfileUpdateForm, UserProductForm


def index(request):
    current_user = request.user

    profile = UserProfile.objects.get(pk=current_user.id)
    context ={'profile': profile, }

    return render(request,'user_profile.html',context)

@login_required(login_url='/login')
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('/user')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {'user_form': user_form,
                   'profile_form': profile_form,
                   }
        return render(request, 'user_update.html', context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Plase correct the arror below.')
            return HttpResponseRedirect('/user/password')

    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'change_password.html', {
            'form': form,
        })

def products_new(request):
    if request.POST:
        form = UserProductForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            data = Product()
            data.user_id = user.id
            data.category_id = request.POST.get('category')
            data.title = form.cleaned_data['title']
            data.description = form.cleaned_data['description']
            data.keywords = form.cleaned_data['keywords']
            data.image = form.cleaned_data['image']
            data.price = form.cleaned_data['price']
            data.amount = form.cleaned_data['amount']
            data.detail = form.cleaned_data['detail']
            data.slug = form.cleaned_data['slug']
            data.status = 'False'
            data.save()

            messages.success(request,'İlanınız Başarıyla Eklendi <a href=/product/'+str(data.id)+'/'+str(data.slug)+'">İlanı incele-></a>')
            return HttpResponseRedirect('/user/productsnew')
        else:
            messages.error(request, 'Ürün ekleme hatalı...')
            return HttpResponseRedirect('/user/productsnew')
    else:
        form = UserProductForm()
        user = request.user
        current_user = UserProfile.objects.get(user_id=user.id)
        context = {'profile': current_user,
                   'form': form,
                   }
        return render(request, 'user_products_new.html',context)










