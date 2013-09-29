from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import contractions.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pregnancy.views.home', name='home'),
    # url(r'^pregnancy/', include('pregnancy.foo.urls')),
    url(r'^contractions/$', contractions.views.ContractionList.as_view(), name='ContractionList'),
    url(r'^update_intensity/(?P<pk>\d+)/$', contractions.views.UpdateIntensity.as_view(), name='UpdateIntensity'),
    url(r'^update_intensity2/(?P<pk>\d+)/$', contractions.views.UpdateIntensity2.as_view(), name='UpdateIntensity2'),
    url(r'^ContractionListTable/$', contractions.views.ContractionListTable.as_view(), name='ContractionListTable'),
    url(r'^StartContraction/$', contractions.views.StartContraction.as_view(), name='StartContraction'),
    url(r'^StopContraction/(?P<pk>\d+)/$', contractions.views.StopContraction.as_view(), name='StopContraction'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
