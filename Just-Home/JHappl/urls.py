from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.HomePageView.as_view(), name='home'),
    path('upload/', views.UploadPageView.as_view(), name='upload'),
    path('success/', views.SuccessPageView.as_view(), name='success'),
    path('failure/', views.FailurePageView.as_view(), name='failure')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
