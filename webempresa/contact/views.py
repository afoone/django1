from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()
    if (request.method == "POST"):
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            content = request.POST.get('content')
            #Enviamos el correo
            email = EmailMessage(
                'Nuevo contacto',
                'de {} {} Escribió {}'.format(name, email, content),
                'atienda@iprocuratio.com',
                ['pruebas@mailinator.com'], reply_to=None
            )
            try:
                email.send()
            except:
                return redirect(reverse('contact')+'?fail')
            return redirect(reverse('contact')+'?ok')
        else:
            return render(request, 'contact/contact.html', {'form': contact_form})
    else:
        return render(request, 'contact/contact.html', {'form': contact_form})
