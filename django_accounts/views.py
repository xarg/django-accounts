import base64

from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect

def login(REQUEST):
    if 'HTTP_AUTHORIZATION' in REQUEST.META:
        auth_data = REQUEST.META['HTTP_AUTHORIZATION'].split()
        if len(auth_data) == 2:
            if auth_data[0].lower() == "basic":
                uname, passwd = base64.b64decode(auth_data[1]).split(':')
                user = auth.authenticate(username=uname, password=passwd)
                if user is not None and user.is_active:
                    auth.login(REQUEST, user)
                    return HttpResponseRedirect(REQUEST.GET.get('next', '/'))
    response = HttpResponse()
    response.status_code = 401
    response['WWW-Authenticate'] = 'Basic realm="Django Accounts"'
    return response

def logout(REQUEST):
    auth.logout(REQUEST)
    return HttpResponseRedirect(REQUEST.GET.get('next', '/'))
