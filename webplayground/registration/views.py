from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms
from .forms import UserCreationFormWithEmail

class SingUpView(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'registration/registration.html'

    def get_success_url(self):
        return reverse_lazy ('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SingUpView, self).get_form()
        # modificar en tiempo real 
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder' : 'Usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder' : 'Correo-e'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder' : 'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder' : 'Repetir contraseña'})

        return form