from django.shortcuts import render
from django.http import HttpResponse
from cms.models import Pages

# Create your views here.
# 1. Metodo para mostrar todo lo que tenemos en la basa de datos
# 2. Metodo para mostrar lo que nos pidan si lo tenemos en la base de datos

def showAll(request):
    lista = Pages.objects.all()
    respuesta = "<h2>BASE DE DATOS</h2>"
    idAux = 1
    #lo imprimimos con forma de lista con <li>
    if len(lista) != 0:
        lista_pags = Pages.objects.all()
        for pag in lista_pags:
            respuesta+="<h4><li>Id: " + str(idAux) + " | " + pag.name + " : " + pag.page + "</li></h4>"
            idAux += 1
    else :
        respuesta = "La base de datos esta vacia."
    return HttpResponse(respuesta)

def showOne(request, identificador):
    try:
        page = Pages.objects.get(id=identificador)
        respuesta = "Has elegido " + page.name + ". Su pagina es: " + page.page + ". Su id es: " + str(page.id)
    except Pages.DoesNotExist:
        respuesta = "No existe pagina con el identificador " + str(identificador) + "."
    return HttpResponse(respuesta)

# def savePage(request,name,page):
#     pagina = Pages(name=name,page=page)
#     lista = Pages.objects.all()
#     guardado = False
#     for pages in lista:
#         if pages.name == name:
#             guardado = True
#     if guardado != True:
#         pagina.save()
#         respuesta = "Se ha guardado la pagina: " + name \
#                     + ". Se ha guardado con identificador " + str(pagina.id)
#     else:
#         respuesta = "Ya teniamos guardada la pagina " + name
#     return HttpResponse(respuesta)
