from django.urls import path, include
from django.contrib import admin
from . import views
from .views import PreuzmiStanjeView

app_name = "artikli"

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
    path("<int:artikl_id>/", views.artikl, name="artikl"),
    path("stanje/", views.prikaz_stanja, name="prikaz_stanja"),
    path("unos_stanja/", views.unos_stanja, name="unos_stanja"),
    path("stanje/preuzmi/", views.preuzmi_stanje, name="preuzmi_stanje"),
]
