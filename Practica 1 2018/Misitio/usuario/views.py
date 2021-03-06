# -*- coding: utf-8 -*-
import datetime
from flask import request
from models import Usuarios
from models import Textos
from django.views import generic
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
from .forms import TextForm
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.core.urlresolvers import reverse

a=""
# Create your views here.
class IndexView(TemplateView):
    template_name='usuario/index.html'

def mandarCorreo(username):
    #client_ip = request.META.get('HTTP_X_FORWARDED_FOR') 
    now = datetime.datetime.now()
    mail_subject = 'Notificación de Ingreso'
    message = "Hola tu fecha, hora e ip de ingreso son: "+str(now.day)+"/"+str(now.month)+"/"+str(now.year)+ ", " +str(now.hour)+":"+str(now.minute) #+ ", " #+client_ip           
    to_email=Usuarios.objects.get(pk=username).Correo
    email = EmailMessage(
        mail_subject, message, to=[to_email]
    )
    email.send()

def detail(request,Usuario):
    if a==Usuario: 
        text=get_object_or_404(Usuarios,pk=Usuario)
        p=Textos.objects.all()
        return render(request,'usuario/detail.html',{'text':text,'p':p})
    else: 
        return redirect('usuario:index')

class UsuarioCreate(View):
    form_class=UserForm
    template_name='usuario/registration_form.html'
    def get(self, request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})
    def post(self, request):
        form=self.form_class(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            username=form.cleaned_data['Usuario']
            password=form.cleaned_data['contrasena']
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activa tu cuenta.'
            message = render_to_string('usuario/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email=Usuarios.objects.get(pk=username).Correo
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Por favor confirma tu correo para continuar')
        return render(request,self.template_name,{'form':form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = Usuarios.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Usuarios.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.EstaActivo="Si"
        user.save()
        global a
        a=user.Usuario
        # return redirect('home')
        mandarCorreo(user.Usuario)
        return redirect('usuario:detail', user.Usuario)
        
    else:
        return HttpResponse('Activation link is invalid!')


class LogIn(View):
    form_class=UserForm
    template_name='usuario/login.html'
    def get(self, request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})
    def post(self, request):
        form=self.form_class(request.POST)
        username = request.POST['Usuario']
        password = request.POST['contrasena']
        try: 
            user=Usuarios.objects.get(pk=username)
            if user.contrasena==password and user.EstaActivo=="Si": 
                global a
                a=username
                mandarCorreo(username)
                return redirect('usuario:detail', username)
            else: 
                return render(request,self.template_name,{'form':form})
        except Usuarios.DoesNotExist: 
            return render(request,self.template_name,{'form':form})
            
class UsuarioUpdate(UpdateView):
    model=Usuarios
    fields=['Carrera', 'Nombres', 'Apellidos', 'Correo', 'CUI','contrasena']




class UsuarioTexto(CreateView):
    form_class=TextForm
    template_name='usuario/textos_form.html'
    def upload(request):
        if request.method == 'POST':
            form = TextForm(request.POST, request.FILES)
            if form.is_valid():
                obj = form.save()
    def get_success_url(self):
            return reverse('usuario:index')

def display_texto_view(request):
    documento = Texto.objects.get(nombre='doc2')
    x_file= open(path +"\media\\archivos\\"+ 'doc2' +".pdf","r")
    data= x_file.read()
    personas=[]
    for i in list:
        personas.append(str(i)+".jpg")
    return render(request, 'usuario/analizador.html', {'data':data, 'images':imagenes})


                





