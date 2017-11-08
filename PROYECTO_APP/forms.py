from django import forms
from PROYECTO_APP.models import Encabezado, Material

class EncabezadoForm(forms.ModelForm):
     class Meta:
        model = Encabezado
        fields = ('fecha', 'encargado', 'materiales')

def __init__ (self, *args, **kwargs):
        super(PeliculaForm, self).__init__(*args, **kwargs)
        self.fields["materiales"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["materiales"].help_text = "Ingrese los materiales de la orden de compra"
        self.fields["materiales"].queryset = Actor.objects.all()


class MaterialForm(forms.ModelForm):
     class Meta:
        model = Material
        fields = ('nombre', 'unidad', 'precio')
