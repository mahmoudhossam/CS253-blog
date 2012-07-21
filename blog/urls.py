from django.conf.urls import patterns, include, url
from webapp import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
        url(r'^newpost$', views.newpost),
        url(r'^$', views.allposts),
        url(r'^post/(?P<post_id>\d+)$', views.post),
        url(r'^post/(?P<post_id>\d+).json$', views.post_json),
        url(r'^signup$', views.signup),
        url(r'^welcome$', views.welcome),
        url(r'^login$', views.login),
        url(r'^logout$', views.logout),
        url(r'^.json$', views.all_json),
        url(r'^flush$', views.flush_cache),
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
