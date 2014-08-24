from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from bookservices import views
admin.autodiscover()

urlpatterns = patterns(#'',
    # Examples:
    # url(r'^$', 'bookbeeper.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^',include(router.urls)),
    #url(r'^api-auth',include('rest_framework.urls',namespace='rest_framework')),
    '',
    url(r'^library/$',views.LibraryBookList.as_view()),
    url(r'^library/(?P<pk>[0-9]{13})/$',views.LibraryBookIndividual.as_view()),
    url(r'^library/import/(?P<pk>[0-9]{13})/$', views.LibraryBookImporterView.as_view())
)

urlpatterns = format_suffix_patterns(urlpatterns)