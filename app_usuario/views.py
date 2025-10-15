from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario

# Listar usuarios
def index(request):
    usuarios = Usuario.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})

# Ver usuario (opcional)
def ver_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    return render(request, 'ver_usuario.html', {'usuario': usuario})

# Agregar usuario
def agregar_usuario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        telefono = request.POST['telefono']
        email = request.POST['email']
        edad = request.POST['edad']
        
        Usuario.objects.create(
            nombre=nombre,
            apellido=apellido,
            telefono=telefono,
            email=email,
            edad=edad
        )
        return redirect('inicio')
    return render(request, 'agregar_usuario.html')

# Editar usuario
def editar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        usuario.nombre = request.POST['nombre']
        usuario.apellido = request.POST['apellido']
        usuario.telefono = request.POST['telefono']
        usuario.email = request.POST['email']
        usuario.edad = request.POST['edad']
        usuario.save()
        return redirect('inicio')
    return render(request, 'editar_usuario.html', {'usuario': usuario})

# Borrar usuario
def borrar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('inicio')
    return render(request, 'borrar_usuario.html', {'usuario': usuario})
