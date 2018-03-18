from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^follow/$', views.user_follow, name='follow'),
    url(r'^(?P<user_id>\d+)/profile/$', views.profile, name='profile'),
    url(r'^edit/profile/$', views.edit_profile, name='edit_profile'),
    url(r'following/actions/$', views.following_actions, name='following_actions')
]
