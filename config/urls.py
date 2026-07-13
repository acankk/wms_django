from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)
urlpatterns = [
    path("admin/", admin.site.urls),


    path("api/", include("apps.users.urls")),
    path("api/", include("apps.master.urls")),
    path("api/", include("apps.stock.urls")),
    
    path("api/", include("apps.inventory.urls")),
    path("api/", include("apps.inbound.urls")),
    path("api/outbounds/", include("apps.outbound.urls")),
    path(
        "api/reports/",
        include("apps.reports.urls"),
    ),

    path(
        "api/schema/",
        SpectacularAPIView.as_view(),
        name="schema",
    ),

    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(
            url_name="schema"
        ),
        name="swagger-ui",
    ),

]