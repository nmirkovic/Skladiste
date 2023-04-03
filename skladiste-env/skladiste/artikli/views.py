from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Artikl, Stanje, Lokacija, JedinicaMjere
import openpyxl, barcode
from django.http import HttpResponse
from barcode.writer import ImageWriter
from docx import Document
from docx.shared import Cm, Inches
from PIL import Image
import os


def index(request):
    lista_artikala = Artikl.objects.order_by("naziv_artikla")[:5]
    context = {
        "lista_artikala": lista_artikala,
    }
    return render(request, "artikli/index.html", context)


def artikl(request, artikl_id):
    artikl = get_object_or_404(Artikl, pk=artikl_id)
    context = {
        "artikl": artikl,
    }
    return render(request, "artikli/artikl.html", context)


def prikaz_stanja(request):
    stavke = Stanje.objects.all()
    context = {"stavke": stavke}
    return render(request, "artikli/stanje.html", context)


def unos_stanja(request):
    if request.method == "POST":
        artikl_id = request.POST.get("artikl_id")
        lokacija_id = request.POST.get("lokacija_id")
        jedinica_mjere_id = request.POST.get("jedinica_mjere_id")
        kolicina = request.POST.get("kolicina")
        datum = request.POST.get("datum")

        artikl = get_object_or_404(Artikl, id=artikl_id)
        lokacija = get_object_or_404(Lokacija, id=lokacija_id)
        jedinica_mjere = get_object_or_404(JedinicaMjere, id=jedinica_mjere_id)

        stanje = Stanje.objects.create(
            artikl_id=artikl,
            lokacija_id=lokacija,
            jedinica_mjere_id=jedinica_mjere,
            kolicina=kolicina,
            datum=datum,
        )

        return redirect("artikli:prikaz_stanja")

    artikli = Artikl.objects.all()
    lokacije = Lokacija.objects.all()
    jedinice_mjere = JedinicaMjere.objects.all()

    context = {
        "artikli": artikli,
        "lokacije": lokacije,
        "jedinice_mjere": jedinice_mjere,
    }
    return render(request, "artikli/unos_stanja.html", context)


def preuzmi_stanje(request):
    stanja = Stanje.objects.all()
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Artikl", "Lokacija", "Jedinica mjere", "Količina", "Datum"])

    for stanje in stanja:
        datum = timezone.localtime(stanje.datum).replace(tzinfo=None)
        ws.append(
            [
                stanje.artikl_id.naziv_artikla,
                stanje.lokacija_id.naziv_lokacije,
                stanje.jedinica_mjere_id.naziv_mjere,
                stanje.kolicina,
                datum,
            ]
        )

    response = HttpResponse(content_type="application/ms-excel")
    response["Content-Disposition"] = 'attachment; filename="stanje.xlsx"'

    wb.save(response)

    return response
