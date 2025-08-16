"""
URL configuration for ecom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from store import views
from django.views.generic.base import RedirectView



from . import settings
from django.conf.urls.static import static
app_name = 'store'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('store.urls')),
    # English site URLs with proper namespace
    path('en/', include(('store.urls_en', 'store'), namespace='en')),

    # Optional: Myanmar site
    path('mm/', include(('store.urls_mm', 'store'), namespace='mm')),

    path('cart/',include('cart.urls')),
    path('payment/',include('payment.urls')),
]
