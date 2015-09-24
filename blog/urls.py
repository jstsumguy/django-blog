from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import *

urlpatterns = patterns('',
    url(r'^$', 'posts.views.home', name='home'),
    url(r'^tag/(?P<tag_id>\d+)/$', 'posts.views.tag'),
    url(r'^post/(?P<post_id>\d+)/$', 'posts.views.post'),
    
    url(r'^edit_post/$', 'posts.views.edit_post'),
    url(r'^create_comment/$', 'posts.views.create_comment'),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^signup/$', 'posts.views.signup'),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
