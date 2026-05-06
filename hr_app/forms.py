from django import forms
from .models import Employe, Departement, Contrat

class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = ['nom', 'prenom', 'type_poste', 'salaire', 'date_embauche', 'dernier_diplome', 'departement']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'type_poste': forms.Select(attrs={'class': 'form-select'}),
            'salaire': forms.NumberInput(attrs={'class': 'form-control'}),
            'date_embauche': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'dernier_diplome': forms.TextInput(attrs={'class': 'form-control'}),
            'departement': forms.Select(attrs={'class': 'form-select'}),
        }
