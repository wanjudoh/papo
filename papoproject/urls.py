from django.contrib import admin
from django.urls import path, include
import account.views
from django.conf import settings
from django.conf.urls.static import static
import comment.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('market/', include('market.urls')),
    path('msg/', include('msg.urls')),
    path('', account.views.home, name="home"),
    path('comment/', include('comment.urls')),
    path('profile/', include('myprofile.urls')),
    path('honeytip/', include('honeytip.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)