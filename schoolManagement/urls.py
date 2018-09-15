from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from schoolManagement.views import HomePage
app_name="School management"

urlpatterns = [
    path('', HomePage),
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('review/', include('review.urls')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)