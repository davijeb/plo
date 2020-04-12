from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('ploadmin/', include('ploadmin.urls')),
    path('admin/', admin.site.urls),
]