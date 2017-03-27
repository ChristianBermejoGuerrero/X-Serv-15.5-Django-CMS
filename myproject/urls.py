from django.conf.urls import patterns, include, url
from django.contrib import admin
from cms import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.showAll, name='mostrar todo'),
    #url(r'(.+)/(.+)$', views.savePage,name='guardar pagina'),
    url(r'^(.+)$', views.showOne, name='mostrar uno'),
    url(r'^admin/', include(admin.site.urls)),
)
