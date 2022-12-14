
from django.contrib import admin
from django.urls import path, include
from demo import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #all-auth path
    path('accounts/', include('allauth.urls')),
    path('', include('loginapp.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
