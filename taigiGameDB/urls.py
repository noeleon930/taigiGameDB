from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'taigiGameDB.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', 'queryClosePronounce.views.hello_world'),
    url(r'^q/close_pronounce/(?P<pronounceQ>.+)/$', 'queryClosePronounce.views.query'),
    url(r'^q/chinese_word/(?P<wordQ>.+)/$', 'queryChinese.views.query'),
]
