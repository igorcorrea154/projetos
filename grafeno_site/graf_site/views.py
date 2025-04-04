from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Token
import secrets
from django.http import HttpResponseForbidden

def get_client_ip(request):
    """ Obtém o IP do usuário """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def generate_token(request):
    """ Gera um token e salva na sessão """
    ip = get_client_ip(request)
    existing_token = Token.objects.filter(ip_address=ip).order_by('-created_at').first()

    if existing_token and existing_token.is_valid():
        token = existing_token.token
    else:
        token = secrets.token_urlsafe(32)
        Token.objects.create(ip_address=ip, token=token)

    request.session['user_token'] = token  # 🔥 Armazena o token na sessão
    return redirect('linkvertise_page')  # 🔄 Redireciona para a página do Linkvertise

def linkvertise_page(request):
    """ Página intermediária para passar pelo Linkvertise """
    return render(request, 'linkvertise.html')  # 🔄 Crie esse template


def mostrar_token(request):
    """ Exibe o token após o usuário passar pelo Linkvertise """
    token = request.session.get('user_token')

    if not token:
        return HttpResponseForbidden("❌ Você ainda não passou pelo Linkvertise.")

    return render(request, 'token_page.html', {'token': token})
