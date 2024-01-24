"""
URL configuration for python_jmc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include

#Django settings
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('index.urls')),
    path('empresa/',include('empresa.urls')),
    path('mantenimiento/',include('mantenimiento.urls')),
    path('sWeb/',include('sWeb.urls')),
    path('menuAspel/',include('menuAspel.urls')),
    path('login/',include('login.urls')),
    path('inicioAdmin/',include('inicioAdmin.urls')),
    path('inicio_cliente/',include('inicio_cliente.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
]
# Configuración para servir archivos multimedia en modo de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)