"""coolsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from coolsite import settings
from django.urls import path
from honey.views import *
from rest_framework import routers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('api/v1/DjangoProject-auth/', include('rest_framework.urls')),
    path('api/v1/honey/', HoneyAPIList.as_view()),
    path('api/v1/honey/<int:pk>/', HoneyAPIUpdate.as_view()),
    path('api/v1/honeydelete/<int:pk>/', HoneyAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('', include('honey.urls')),
]

# handler404 = not_found
# handler403 = closed_access
# handler400 = bad_request




if settings.DEBUG:
    import debug_toolbar

    urlpatterns =[
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
