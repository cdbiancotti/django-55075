from django import forms

class CursoFormularioBase(forms.Form):
    titulo = forms.CharField(max_length=50)
    numero = forms.IntegerField()


class CrearCursoFormulario(CursoFormularioBase):
    ...
    
    
class EditarCursoFormulario(CursoFormularioBase):
    ...
    
    
class CursoBusquedaFormulario(forms.Form):
    titulo = forms.CharField(max_length=50, required=False)