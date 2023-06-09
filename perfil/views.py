from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from . import forms


class BaseView(View):
    templates_name = 'perfil/index.html'

    def setup(self,  *args, **kwargs):
        super().setup( *args, **kwargs)
        self.contexto = {
            'usuario': forms.UsuarioForms(
                data=self.request.POST or None
            ),
            'login': forms.UsuarioLogin(
                data=self.request.POST or None
            ),
        }
        self.usuarioBanco = self.contexto['usuario']
        self.page = render(self.request,self.templates_name, self.contexto)
    def get(self, *args, **kwargs):
        return self.page
class Login(BaseView):
    def post(self, *args, **kwargs):


        senha = self.request.POST.get('password')
        usuario = self.request.POST.get('username').lower()
        print(senha)
        print(usuario)
        user = authenticate(self.request, username=usuario, password=senha)
        if not user:
            messages.error(
                self.request,
                "Usuario ou senha invalidos"
            )
            return redirect('perfil:login')

        login(self.request, user=user)
        messages.success(
            self.request,
            "Login efetuado com sucesso"
        )
        return redirect('produtos:home')

class Cadastro(BaseView):
    templates_name = 'perfil/register.html'
    def get(self, *args, **kwargs):
        return self.page
    def post(self, *args, **kwargs):
        if not self.usuarioBanco.is_valid():
            messages.error(
                self.request,
                self.usuarioBanco.errors
            )

            return self.page
        senha = self.request.POST.get('password')
        usuario = self.request.POST.get('username')

        usuario_db = self.usuarioBanco.save(commit=False)
        usuario_db.set_password(senha)
        usuario_db.username = usuario.lower()
        usuario_db.save()
        return redirect('perfil:login')
class Logout(View):
    def get(self, *args, **kwargs):
        logout(self.request)
        return redirect('perfil:login')
