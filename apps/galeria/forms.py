from django import forms
from .models import Fotografia


class FotografiaForms(forms.ModelForm):
    class Meta: # faz referencia ao metadados da classe fotografia
        model = Fotografia
        exclude = ['publicada', ] # exclui o campo publicada do formulario
        labels = {  # customizando os labels do formulario
            'descricao': 'Descrição',
            'data_fotografia': 'Data de Registro',
            'usuario': 'Usuário',
        }


        # customizando os widgets do formulario (css)
        widgets = {
            'nome' : forms.TextInput(attrs={'class': 'form-control' }),
            'legenda' : forms.TextInput(attrs={'class': 'form-control' }),
            'categoria' : forms.Select(attrs={'class': 'form-control' }),
            'descricao' : forms.Textarea(attrs={'class': 'form-control'}), # Textarea para campo maior
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'data_fotografia': forms.DateInput(format='%d-%m-%Y', attrs={'type': 'date', 'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
        }

