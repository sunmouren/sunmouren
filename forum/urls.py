from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<post_id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^new_post/$', views.new_post, name='new_post'),
    url(r'^edit_post/(?P<post_id>\d+)/$', views.edit_post, name='edit_post'),
    url(r'^post/like/$', views.post_like, name='post_like'),
]