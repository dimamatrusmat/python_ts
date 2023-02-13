from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('convert/', include('exchange_v.urls')),
    path('fioget/', include('fioget.urls')),
    path('recorder/', include('voice_recorder.urls')),
]
