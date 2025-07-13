from django.http import HttpResponse

def teste_view(request):
    return HttpResponse("Teste")

def index_view(request):
    return HttpResponse("Bem vindo")