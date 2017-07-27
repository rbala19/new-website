from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'internal'
urlpatterns = [
    url(r'^$', auth_views.login, {'template_name': 'internal/login.html'}, name='login'),
    url(r'^events/$', views.event_list, name='event_list'),
    url(r'^members/$', views.member_list, name='member_list'),
    url(r'^register/$', views.register, name='register'),
    url(r'^events/(?P<event_name>.+)/$', views.event_details, name='event_details'),
    url(r'^members/(?P<username>.+)/$', views.member_details, name='member_details'),
]
