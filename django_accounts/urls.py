from django.conf.urls.defaults import *
from accounts import views

urlpatterns = patterns('',
    url(r'^login/', views.login, name="login"),
    url(r'^logout/', views.logout, name="logout")
)