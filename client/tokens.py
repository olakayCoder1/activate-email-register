import random
import string






length = 100


ran = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k = length ))





"""user_mail = request.POST['email']
        if form.is_valid():
            print('kabiru')
            user = form.save(commit=False)
            user.is_active = False 
            token = get_tok()   
            try:
                template = render_to_string('client/confirm-mail.html', {'usern': user ,
                'uid': urlsafe_base64_encode(force_bytes(user.id)),
                'token': token, 'domain': get_current_site(request)
                })

                """