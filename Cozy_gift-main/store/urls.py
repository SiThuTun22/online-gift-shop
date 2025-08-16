from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import get_object_or_404

from django.views.generic.base import RedirectView
urlpatterns = [
  
     # Include English URLs under /en/
    path('en/', include(('store.urls_en', 'store'), namespace='en')),
    

    # Include Myanmar URLs under /mm/
    path('mm/', include(('store.urls_mm', 'store'), namespace='mm')),

 # Redirect root URL '/' to default language home page, e.g., /en/home/
    path('', RedirectView.as_view(url='/en/home/', permanent=False)),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

