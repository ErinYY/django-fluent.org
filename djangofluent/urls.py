from django.conf.urls import *
from django.conf import settings
from django.contrib import admin
from fluent_pages.sitemaps import PageSitemap
from frontend.views import TextFileView

admin.autodiscover()

sitemaps = {
    # Place sitemaps here
    'pages': PageSitemap,
}

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/filebrowser/', include('filebrowser.urls')),
    url(r'^admin/util/tools/', include('admin_tools.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )

def view500(request):
    raise NotImplementedError("500 error page test")

# Include all remaining pages URLs from the CMS
urlpatterns += patterns('',
    url(r'^500test/$', view=view500),
    url(r'^404/$', 'django.views.defaults.page_not_found'),
    url(r'^500/$', 'django.views.defaults.server_error'),

    # SEO API's
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^robots.txt$', TextFileView.as_view(content_type='text/plain', template_name='robots.txt')),

    # CMS modules
    url(r'', include('fluent_pages.urls')),
)
