from django.forms import ModelForm
from django.shortcuts import render, redirect

# Create your views here.
from notes.models import Alumne


def llistat_alumnes(request):
    alumnes = Alumne.objects.all()
    return render(request, "llistat_alumnes.html", {"alumnes": alumnes})


def detalls_alumne(request, id_alumne):
    alumne = Alumne.objects.get(id=id_alumne)
    return render(request, "detalls_alumne.html", {"alumne": alumne})


class FormAlumne(ModelForm):
    class Meta:
        model = Alumne
        fields = "__all__"


def agregar_alumne(request):
    if request.method == "POST":
        form = FormAlumne(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="llistat_alumnes")
    else:
        form = FormAlumne()

    return render(request, "agregar_alumne.html", {"form": form})


def modificar_alumne(request, id_alumne):
    alumne = Alumne.objects.get(id=id_alumne)

    if request.method == "POST":
        form = FormAlumne(request.POST, instance=alumne)
        if form.is_valid():
            form.save()
            return redirect(to="llistat_alumnes")
    else:
        form = FormAlumne(instance=alumne)

    return render(request, "modificar_alumne.html", {"form": form})


def borrar_alumne(request, id_alumne):
    alumne = Alumne.objects.get(id=id_alumne)

    if request.method == "POST":
        alumne.delete()
        return redirect(to="llistat_alumnes")

    return render(request, "confirma_borrat.html")


