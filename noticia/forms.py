from django import forms
from .models import formulario



    class formularioForm(forms.ModelForm):
    name = forms.CharField(label='name',max_length=200, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    email = forms.CharField(label='email', max_length=100, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    telefono = forms.CharField(label='telefono', max_length=100,widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    message = forms.CharField(label='message', max_length=1000, widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))
     class Meta:
        model = Movie
        fields = ('name','email','telefono', 'message',)