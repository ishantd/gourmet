from django.conf import settings
from django.contrib import messages
from django.utils.encoding import force_bytes
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from accounts.models import UserProfile
from accounts.forms import SignupForm


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
            mail.send(
                [to_email],
                subject=mail_subject,
                sender=settings.EMAIL_HOST_USER,
                message=message,
                priority='now',
            )
            messages.success(request, "You've successfully registered!")
            messages.info(request,
                          "Please verify your email address, we've sent you a mail at your registered email ID.")
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = SignupForm()
    return render(request, 'accounts/register.html', {'form': form})