from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^entry/$', views.submit_comment, name='submit_comment'),
    url(r'^reply/$', views.submit_reply, name='submit_reply'),
    url(r'^favour/$', views.submit_favour, name='submit_favour'),
]
