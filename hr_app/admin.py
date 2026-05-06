from django.contrib import admin
from .models import Departement, Employe, Contrat

@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    list_display = ('nom_service', 'lieu', 'responsable')
    search_fields = ('nom_service', 'lieu')

@admin.register(Employe)
class EmployeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'type_poste', 'salaire', 'date_embauche', 'departement', 'est_archive')
    list_editable = ('type_poste', 'salaire', 'departement', 'est_archive')
    list_filter = ('type_poste', 'departement', 'est_archive', 'date_embauche')
    search_fields = ('nom', 'prenom', 'dernier_diplome')
    date_hierarchy = 'date_embauche'

@admin.register(Contrat)
class ContratAdmin(admin.ModelAdmin):
    list_display = ('employe', 'type_contrat', 'date_fin')
    list_filter = ('type_contrat',)
