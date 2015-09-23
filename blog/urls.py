from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import *

urlpatterns = patterns('',
    url(r'^$', 'posts.views.home', name='home'),
    url(r'^tag/(?P<tag_id>\d+)/$', 'posts.views.tag'),
    url(r'^edit_post/$', 'posts.views.edit_post'),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
