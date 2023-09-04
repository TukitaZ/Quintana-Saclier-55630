from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import *
from .forms import *

# CBV #
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

# Login y Logout #
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
    return render(request, 'aplicacion/home.html')

@login_required
def materias(request):
    contexto = {'materias': Materia.objects.all()}
    return render(request, 'aplicacion/materias.html', contexto)

@login_required
def maestros(request):
    contexto = {'maestros': Maestro.objects.all()}
    return render(request, 'aplicacion/maestros.html', contexto)

@login_required
def alumnos(request):
    contexto = {'alumnos': Alumno.objects.all()}
    return render(request, 'aplicacion/alumnos.html', contexto)

@login_required
def directores(request):
    contexto = {'directores': Director.objects.all()}
    return render(request, 'aplicacion/directores.html', contexto)

@login_required
def BuscarMaestro(request):
    return render(request, 'aplicacion/BuscarMaestro.html')

def buscar1(request):
    if request.GET.get('buscar'):
        patron = request.GET.get('buscar')
        maestros = Maestro.objects.filter(nombre__icontains=patron) or Maestro.objects.filter(apellido__icontains=patron)
        contexto = {'maestros': maestros, 'titulo': f'Alumnos que tienen como patron, "{patron}"'}
        return render(request, 'aplicacion/maestros.html', contexto)
    return HttpResponse('No se ingreso nada a buscar')

@login_required
def BuscarMateria(request):
    return render(request, 'aplicacion/BuscarMateria.html')

def buscar2(request):
    if request.GET.get('buscar'):
        patron = request.GET.get('buscar')
        materias = Materia.objects.filter(nombre__icontains=patron)
        contexto = {'materias': materias, 'titulo': f'Materias que tienen como patron, "{patron}"'}
        return render(request, 'aplicacion/materias.html', contexto)
    return HttpResponse('No se ingreso nada a buscar')

@login_required
def BuscarAlumno(request):
    return render(request, 'aplicacion/BuscarAlumno.html')

def buscar3(request):
    if request.GET.get('buscar'):
        patron = request.GET.get('buscar')
        alumnos = Alumno.objects.filter(nombre__icontains=patron) or Alumno.objects.filter(apellido__icontains=patron)
        contexto = {'alumnos': alumnos, 'titulo': f'Alumnos que tienen como patron, "{patron}"'}
        return render(request, 'aplicacion/alumnos.html', contexto)
    return HttpResponse('No se ingreso nada a buscar')

@login_required
def BuscarDirector(request):
    return render(request, 'aplicacion/BuscarDirector.html')

def buscar4(request):
    if request.GET.get('buscar'):
        patron = request.GET.get('buscar')
        directores = Director.objects.filter(nombre__icontains=patron) or Director.objects.filter(apellido__icontains=patron)
        contexto = {'directores': directores, 'titulo': f'Directores que tienen como patron, "{patron}"'}
        return render(request, 'aplicacion/directores.html', contexto)
    return HttpResponse('No se ingreso nada a buscar')

# Class Based View Alumnos#

class AlumnosList(LoginRequiredMixin, ListView):
    model = Alumno

class AlumnosCreate(LoginRequiredMixin, CreateView):
    model = Alumno
    fields = ['nombre','apellido','documento','email','comision']
    success_url = reverse_lazy('alumnos')

class AlumnosUpdate(LoginRequiredMixin, UpdateView):
    model = Alumno
    fields = ['nombre','apellido','documento','email','comision']
    success_url = reverse_lazy('alumnos')

class AlumnosDelete(LoginRequiredMixin, DeleteView):
    model = Alumno
    success_url = reverse_lazy('alumnos')

# Class Based View Materias #

class MateriasList(LoginRequiredMixin, ListView):
    model = Materia

class MateriasCreate(LoginRequiredMixin, CreateView):
    model = Materia
    fields = ['nombre','comision']
    success_url = reverse_lazy('materias')

class MateriasUpdate(LoginRequiredMixin, UpdateView):
    model = Materia
    fields = ['nombre','comision']
    success_url = reverse_lazy('materias')

class MateriasDelete(LoginRequiredMixin, DeleteView):
    model = Materia
    success_url = reverse_lazy('materias')

# Class Based View Maestros #

class MaestrosList(LoginRequiredMixin, ListView):
    model = Maestro

class MaestrosCreate(LoginRequiredMixin, CreateView):
    model = Maestro
    fields = ['nombre','apellido','documento','email','profesion']
    success_url = reverse_lazy('maestros')

class MaestrosUpdate(LoginRequiredMixin, UpdateView):
    model = Maestro
    fields = ['nombre','apellido','documento','email','profesion']
    success_url = reverse_lazy('maestros')

class MaestrosDelete(LoginRequiredMixin, DeleteView):
    model = Maestro
    success_url = reverse_lazy('maestros')

# Class Based View Directores #

class DirectoresList(LoginRequiredMixin, ListView):
    model = Director

class DirectoresCreate(LoginRequiredMixin, CreateView):
    model = Director
    fields = ['nombre','apellido','documento','turno']
    success_url = reverse_lazy('directores')

class DirectoresUpdate(LoginRequiredMixin, UpdateView):
    model = Director
    fields = ['nombre','apellido','documento','turno']
    success_url = reverse_lazy('directores')

class DirectoresDelete(LoginRequiredMixin, DeleteView):
    model = Director
    success_url = reverse_lazy('directores')

# Login-Logout / Registro

def login_request(request):
    if request.method == 'POST':
        Form = AuthenticationForm(request, data=request.POST)
        if Form.is_valid():
            usuario = Form.cleaned_data.get('username')
            password  = Form.cleaned_data.get('password')
            user = authenticate(username= usuario, password= password)
            if user is not None:
                login(request, user)

                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = '/media/avatares/default.png'
                finally:
                    request.session['avatar'] = avatar
                return render(request, 'aplicacion/home.html', {'mensaje': f'Bienvenido {usuario}'})
            else:
                return render(request, 'aplicacion/login.html', {'form': Form, 'mensaje': f'Los datos son invalidos'})
        else:    
            return render(request, 'aplicacion/login.html', {'form': Form, 'mensaje': f'Los datos son invalidos'})

    Form = AuthenticationForm()

    return render(request, 'aplicacion/login.html', {'form': Form})

def register(request):
    if request.method == 'POST':
        Form = RegistroForm(request.POST)
        if  Form.is_valid():
            usuario = Form.cleaned_data.get('username')
            Form.save()
            return render(request, 'aplicacion/home.html')
    else:    
        Form = RegistroForm()
        
    return render(request, 'aplicacion/registro.html', {'form': Form})

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request, 'aplicacion/home.html')
        else:
            return render(request, 'aplicacion/editarPerfil.html', {'form': form, 'usuario': usuario.username})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, 'aplicacion/editarPerfil.html', {'form': form, 'usuario': usuario.username})

@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():
            usuario = User.objects.get(username=request.user)

            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

            avatar = Avatar(user=usuario, imagen=form.cleaned_data['imagen'])
            avatar.save()

            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar'] = imagen   
            return render(request, 'aplicacion/home.html')
    else:
        form = AvatarForm()
    return render(request, 'aplicacion/agregarAvatar.html', {'form': form })