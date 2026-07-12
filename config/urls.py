from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),


    path("api/", include("apps.users.urls")),
    path("api/", include("apps.master.urls")),
    path("api/", include("apps.stock.urls")),

    path("api/auth/", include("apps.users.urls")),
    
    path("api/", include("apps.inventory.urls")),
    path("api/", include("apps.inbound.urls")),

]