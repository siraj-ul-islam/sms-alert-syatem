from django.contrib import admin
from django.urls import path, include
from user_auth.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin-control-panel/', admin.site.urls),
    path('', include('user_auth.urls')),
    path('dashboard/', include('main_comment_dashboard.urls')),
]
handler404 = "user_auth.views.page_not_found_view"

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
