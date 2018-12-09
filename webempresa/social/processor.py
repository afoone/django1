from .models import Link

# Creamos un diccionario de contexto
def ctx_dic(request):
    enlaces = Link.objects.all()
    ctx = {'enlaces_sociales':enlaces}
    return ctx