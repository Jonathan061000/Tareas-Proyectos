from django.shortcuts import render, redirect
from .models import Configuracion
from .forms import ConfiguracionForm

# Vista para mostrar la lista de configuraciones guardadas
def lista_configuraciones(request):
    configuraciones = Configuracion.objects.all()
    return render(request, 'control/lista_configuraciones.html', {'configuraciones': configuraciones})

# Vista para agregar una nueva configuración
def agregar_configuracion(request):
    if request.method == 'POST':
        form = ConfiguracionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_configuraciones')  # Redirige a la lista de configuraciones
    else:
        form = ConfiguracionForm()
    return render(request, 'control/agregar_configuracion.html', {'form': form})

# Vista para eliminar una configuración
def eliminar_configuracion(request, id):
    configuracion = Configuracion.objects.get(id=id)
    configuracion.delete()
    return redirect('lista_configuraciones')

# Vista para modificar una configuración
def modificar_configuracion(request, id):
    configuracion = Configuracion.objects.get(id=id)
    if request.method == 'POST':
        form = ConfiguracionForm(request.POST, instance=configuracion)
        if form.is_valid():
            form.save()
            return redirect('lista_configuraciones')  # Redirige a la lista de configuraciones
    else:
        form = ConfiguracionForm(instance=configuracion)
    return render(request, 'control/modificar_configuracion.html', {'form': form})
