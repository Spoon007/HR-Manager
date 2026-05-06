from django.db import models
from django.utils import timezone
from datetime import date

class Departement(models.Model):
    nom_service = models.CharField(max_length=100)
    lieu = models.CharField(max_length=100)
    responsable = models.ForeignKey('Employe', on_delete=models.SET_NULL, null=True, blank=True, related_name='dirige')

    def __str__(self):
        return self.nom_service

class Employe(models.Model):
    POSTE_CHOICES = [
        ('Manager', 'Manager'),
        ('Développeur', 'Développeur'),
        ('RH', 'RH'),
        ('Commercial', 'Commercial'),
        ('Autre', 'Autre'),
    ]
    
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    type_poste = models.CharField(max_length=50, choices=POSTE_CHOICES)
    salaire = models.DecimalField(max_digits=10, decimal_places=2)
    date_embauche = models.DateField()
    dernier_diplome = models.CharField(max_length=100)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE, related_name='employes')
    est_archive = models.BooleanField(default=False)

    def calculer_anciennete(self):
        today = date.today()
        diff = today.year - self.date_embauche.year - ((today.month, today.day) < (self.date_embauche.month, self.date_embauche.day))
        return diff

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Contrat(models.Model):
    CONTRAT_CHOICES = [
        ('CDI', 'CDI'),
        ('CDD', 'CDD'),
        ('Stage', 'Stage'),
    ]
    
    employe = models.OneToOneField(Employe, on_delete=models.CASCADE, related_name='contrat')
    type_contrat = models.CharField(max_length=20, choices=CONTRAT_CHOICES)
    date_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Contrat {self.type_contrat} - {self.employe}"
