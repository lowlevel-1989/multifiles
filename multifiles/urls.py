from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from rest_framework import routers

from api.views import TicketViewSet


router = routers.DefaultRouter()
router.register(r'ticket', TicketViewSet)

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='api')),
    url(r'^admin/', admin.site.urls),
    url(r'api/', include(router.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
