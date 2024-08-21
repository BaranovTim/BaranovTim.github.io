
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.add, name='add'),
    path('preaction_first/qrcodes/', include('qrcodes.urls')),
    path('preaction_second/qrcodes/', include('qrcodes.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
