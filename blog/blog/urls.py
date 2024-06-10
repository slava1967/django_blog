"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from main.views import index, contact, robots_txt

from .sitemaps import sitemaps

urlpatterns = [
                  path('sitemap.xml',
                       sitemap,
                       {'sitemaps': sitemaps},
                       name="django.contrib.sitemaps.views.sitemap",
                       ),
                  path('robots.txt', robots_txt, name='robots_txt'),
                  path('slava1967/', admin.site.urls),
                  path('contact/', contact, name='contact'),
                  path('', include('main.urls')),
                  path('', index, name="home"),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
