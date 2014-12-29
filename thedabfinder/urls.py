from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import *
from django.conf import settings
from django.conf.urls.static import static
from django.core.urlresolvers import reverse
admin.autodiscover()

urlpatterns = patterns('',
 url(r'^admin/', include(admin.site.urls)),
    (r'^robots\.txt$',  'pages.views.Robots'),
    (r'^$', 'pages.views.MainHomePage'),
    (r'^avatar/', include('avatar.urls')),
    (r'^tinymce/', include('tinymce.urls')),
    (r'^waxs/$', 'wax.views.WaxsAll'),
    (r'^dispensarys/$', 'wax.views.DispensarysAll'),
    (r'^waxs/(?P<waxslug>.*)/$', 'wax.views.SpecificWax'),
    (r'^dispensarys/(?P<dispensaryslug>.*)/$', 'wax.views.SpecificDispensary'),
    (r'^register/$', 'dabber.views.DabberRegistration'),
    (r'^login/$', 'dabber.views.LoginRequest'),
    (r'^logout/$', 'dabber.views.LogoutRequest'),
    (r'^resetpassword/passwordsent/$', 'django.contrib.auth.views.password_reset_done'),
    (r'^resetpassword/$', 'django.contrib.auth.views.password_reset', {'post_reset_redirect' : '/reset/done/'}),
    (r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm'),
    (r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete'),
    (r'^profile/$', 'dabber.views.UserProfile'),
    (r'^captcha/', include('captcha.urls')),
    (r'^dabgifter/$', 'dabgifter.views.DabGifter'),
    (r'^review/', include('review.urls')),    
    (r'^tou/$',  'pages.views.Tou'),
    (r'^team/$',  'pages.views.Team'),
    (r'^ad/$',  'pages.views.Ad'),
    (r'^contact/$',  'pages.views.Contact'),
)      
if settings.DEBUG:
    urlpatterns += patterns('',
             (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes':True}),
         )

    urlpatterns += patterns('',
            (r'^medias/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
        )



