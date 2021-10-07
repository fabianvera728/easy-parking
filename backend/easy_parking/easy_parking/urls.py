from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include("easy_parking.users.urls")),
                  path('', include("easy_parking.reservations.urls")),
                  path('', include("easy_parking.parking_lots.urls"))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
