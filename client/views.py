from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils.encoding import force_bytes, force_str 
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegistrationForm
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .models import *
import random
import string




def get_tok():
    length = 100
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k = length ))
    return ran




def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        username = request.POST['username']
        user_mail = request.POST['email']
        if form.is_valid():    
            user = form.save(commit=False)
            form.save()
            user.is_active = False 
            token = get_tok()     
            print(urlsafe_base64_encode(force_bytes(user.id)))     
            template = render_to_string('client/confirm-mail.html', {'usern': user ,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': token, 'domain': get_current_site(request)
                })
            email = EmailMessage(
                    'Olakay',
                    template,
                    to=[
                        user_mail
                        ]
                    )
            email.send()
            new_tok = AccountAcivation(user_mail=user_mail, active_token=token)
            new_tok.save()
            return HttpResponse(f'CHECK YOUR MAIL FOR MORE INFO')
        else:
            return HttpResponse('SOMETHING WENT WRONG TRY AGAIN')
    else:
        form = UserRegistrationForm()

        token = 7654
        return render(request, 'client/home.html', {'form': form  , 'token': token})



def activate_account(request, uidb64 , token ):
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and AccountAcivation.objects.filter(active_token=token).exists():  
        user.is_active = True  
        user.save()  
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
    else:  
        return HttpResponse('Activation link is invalid!')  

