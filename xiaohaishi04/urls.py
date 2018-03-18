"""xiaohaishi04 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

import notifications.urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('forum.urls', namespace='forum', app_name='forum')),
    url(r'^users/', include('users.urls', namespace='users', app_name='users')),
    url(r'^comment/', include('two_comment.urls', namespace='two_comment', app_name='two_comment')),
    url(r'^notifications/', include(notifications.urls, namespace='notifications')),
    url(r'^confession/', include('confession_wall.urls', namespace='confession_wall', app_name='confession_wall')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
