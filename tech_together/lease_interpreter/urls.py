from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.upload, name='upload'),
    path('leases/', views.lease_list, name='lease_list'),
    path('leases/uplaod', views.upload_lease, name='upload_lease')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)