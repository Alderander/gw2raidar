from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
        url(r'initial', views.initial, name = "initial"),
        url(r'^(?P<name>encounters|profile|account|register|about|login|index|reset_pw)(?:/(?P<no>\d+))?$', views.named, name = "named"),
        url(r'login.json', views.login, name = "login"),
        url(r'logout.json', views.logout, name = "logout"),
        url(r'register.json', views.register, name = "register"),
        url(r'reset_pw.json', views.reset_pw, name = "reset_pw"),
        url(r'upload.json', views.upload, name = "upload"),
        url(r'change_email.json', views.change_email, name = "change_email"),
        url(r'change_password.json', views.change_password, name = "change_password"),
        url(r'add_api_key', views.add_api_key, name = "add_api_key"),
        url(r'^encounter/(?P<id>\d+)(?P<json>\.json)?$', views.encounter, name = "encounter"),
        url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            auth_views.password_reset_confirm, name='password_reset_confirm'),
        url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
        url(r'^$', views.index, name = "index"),
]
