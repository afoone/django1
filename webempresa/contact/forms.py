from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label = "Nombre", required = True, widget=forms.TextInput(attrs={'class': 'form-control'}), min_length=3, max_length=100)
    email = forms.EmailField(label = "Correo-e", required = True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label = "Mensaje", required = True, widget=forms.Textarea(attrs={'class': 'form-control', 'rows':'3', 'placeholder':'Escribe tu mensaje'}))
    
