from django.shortcuts import render

def inicio(request):
    return render(request,'html/inicio.html')
def sobre(request):
    return render(request, "html/sobre.html")
