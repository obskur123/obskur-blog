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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.shortcuts import redirect
from blog import settings
from dotenv import load_dotenv
import os
load_dotenv()

urlpatterns = [
    path('', lambda req: redirect('blog/home')),
    path('admin/', admin.site.urls),
    path('blog/', include('main.urls'))
] 

if os.getenv('DEBUG') == 'TRUE':
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
