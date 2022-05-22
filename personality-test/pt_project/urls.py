from django.contrib import admin
from django.urls import path,include
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url
# routing information

urlpatterns = [
    path('admin/', admin.site.urls), #default page for django administration
    path('',include('firstapp.urls')), #위임하려는 app의 이름을 두번째 인자에
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
]
#urlpatterns += staticfiles_urlpatterns()
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)