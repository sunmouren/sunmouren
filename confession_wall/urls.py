from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/$', views.get_confessions, name='get_confessions'),
    url(r'^detail/(?P<confession_id>\d+)/$', views.confession_detail, name='confession_detail'),
    url(r'^new//$', views.new_confession, name='new_confession'),
    url(r'^comment/$', views.submit_confession_comment, name='submit_confession_comment'),
    url(r'^reply/$', views.submit_reply_comment, name='submit_reply_comment'),
]
