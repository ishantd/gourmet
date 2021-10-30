from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.utils.encoding import force_bytes
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from accounts.forms import SignupForm
from accounts.models import UserProfile
from accounts.decorators import unauthenticated_user


def Register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            newuser = form.save()
            userprofile, userprofile_created = UserProfile.objects.get_or_create(user=newuser)

            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('accounts/email/acc_activation.html', {
                'user': newuser,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(newuser.pk)),
                'token': default_token_generator.make_token(newuser),
            })
            to_email = form.cleaned_data.get('username')
            send_mail(
                mail_subject,
                message,
                settings.EMAIL_HOST_USER,
                [to_email],
            )
            messages.success(request, "You've successfully registered!")
            messages.info(request,
                          "Please verify your email address, we've sent you a mail at your registered email ID.")
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = SignupForm()
    return render(request, 'accounts/register.html', {'form': form})

@unauthenticated_user
def Login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            userprofile = UserProfile.objects.get(user=user)
            if (userprofile.email_verified == settings.EMAIL_VALIDATION) or (userprofile.email_verified):
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Please confirm your email address.')
        else:
            messages.error(request, 'Username or password is incorrect.')

    return render(request, 'accounts/login.html', context)



def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        userprofile = UserProfile.objects.get(user=user)
        userprofile.email_verified = True
        userprofile.save()
        user.save()
        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('index')
    else:
        return HttpResponse('Activation link is invalid!')
    
@login_required(login_url='/')
def Logout(request):
    logout(request)
    return redirect('index')    