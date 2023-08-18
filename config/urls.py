from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.home.urls', namespace='home')),
    path('shop/', include('apps.shop.urls', namespace='shop')),
    # path('features/', include('apps.home.urls', namespace='features')),
    path('about/', include('apps.about.urls', namespace='about')),
    path('blog/', include('apps.blog.urls', namespace='blog')),
    path('contact', include('apps.contact'
                            '.urls', namespace='contact')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
