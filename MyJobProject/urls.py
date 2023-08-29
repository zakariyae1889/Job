from django.conf import settings
from django.views.static import serve
from django.contrib import admin
from django.urls import path,include,re_path
from django.views.static import serve


handler404="MyJobProject.views.custom_404"

urlpatterns = [
  
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('', include('accounts.urls')),
    path('', include('JobsApp.urls')),
    re_path(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$',serve,{'document_root':settings.STATIC_ROOT}),
   
   
]

