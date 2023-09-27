from django import forms

class CursoFormulario(forms.Form):
    titulo = forms.CharField(max_length=50)
    numero = forms.IntegerField()
    
    
class CursoBusquedaFormulario(forms.Form):
    titulo = forms.CharField(max_length=50, required=False)