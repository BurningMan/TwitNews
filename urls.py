from django.contrib.comments.models import Comment
from django.conf.urls.defaults import patterns, include, url
from views import homepage, categories, fillDatabase
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TwitNews.views.home', name='home'),
    # url(r'^TwitNews/', include('TwitNews.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    ('^$', homepage),
    ('^categories/$', categories),
    ('^filldb/$', fillDatabase),
    #(r'^datetime/plus/(\d{1,2})/$', hours_ahead)
)

# We're going to use the Django server in development, 
# so we'll server also the estatic content.
if settings.DEBUG:
        urlpatterns += patterns('',
           (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'./media/'}),
            (r'^comments/', include('django.contrib.comments.urls')),
        )
