from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('user/', include('accounts.urls')),
    path('recipes/', include('recipes.urls')),
]
