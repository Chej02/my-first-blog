from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib import messages
from PROYECTO_APP.forms import EncabezadoForm, MaterialForm
from PROYECTO_APP.models import Encabezado, Material, Descripcion
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request, 'PROYECTO_APP/index.html')

@login_required
def orden_nueva(request):
    formulario = EncabezadoForm()
    if request.method == "POST":
        formulario = EncabezadoForm(request.POST)
        if formulario.is_valid():
            encabezado = Encabezado.objects.create(fecha=formulario.cleaned_data['fecha'], encargado = formulario.cleaned_data['encargado'])
            for material_id in request.POST.getlist('materiales'):
               descripcion = Descripcion(material_id=material_id, encabezado_id = encabezado.id)
               descripcion.save()
            messages.add_message(request, messages.SUCCESS, 'Orden Guardada Exitosamente')
        else:
            formulario = EncabezadoForm()
    return render(request, 'PROYECTO_APP/orden_editar.html', {'formulario': formulario})

@login_required
def nuevo_material(request):
    formulario = MaterialForm()
    if request.method == "POST":
        formulario = MaterialForm(request.POST)
        if formulario.is_valid():
            post = formulario.save(commit=False)
            post.save()
        messages.add_message(request, messages.SUCCESS, 'Material guardado exitosamente')
    return render(request, 'PROYECTO_APP/new_material.html', {'formulario': formulario})

@login_required
def material_edit(request, pk):
    post = get_object_or_404(Material, pk=pk)
    if request.method == "POST":
        formulario = MaterialForm(request.POST, instance=post)
        if formulario.is_valid():
            post = formulario.save(commit=False)
            post.save()
            return redirect('materiales')
    else:
        formulario = MaterialForm(instance=post)
    return render(request, 'PROYECTO_APP/new_material.html', {'formulario': formulario, 'upnew': "Update Post"})

@login_required
def material_delete(request, pk):
    post = get_object_or_404(Material, pk=pk)
    post.delete()
    return redirect('materiales')

@login_required
def orden_delete(request, pk):
    post = get_object_or_404(Encabezado, pk=pk)
    post.delete()
    return redirect('ordenes')

@login_required
def orden_edit(request, pk):
    post = get_object_or_404(Encabezado, pk=pk)
    if request.method == "POST":
        formulario = EncabezadoForm(request.POST, instance=post)
        if formulario.is_valid():
            post = formulario.save(commit=False)
            post.save()
            for material_id in request.POST.getlist('materiales'):
               descripcion = Descripcion(material_id=material_id, encabezado_id = post.id)
               descripcion.save()

            return redirect('ordenes')
    else:
        formulario = EncabezadoForm(instance=post)
    return render(request, 'PROYECTO_APP/orden_editar.html', {'formulario': formulario, 'upnew': "Update Post"})

def ordenes(request):
    posts = Encabezado.objects.filter().order_by('id')
    return render(request, 'PROYECTO_APP/ordenes.html', {'ordenes': posts})


def materiales(request):
    posts = Material.objects.filter().order_by('id')
    return render(request, 'PROYECTO_APP/materiales.html', {'materiales': posts})
