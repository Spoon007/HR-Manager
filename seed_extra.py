import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hr_manager_project.settings')
django.setup()

from hr_app.models import Employe, Departement, Contrat

def seed_extra():
    # Get departments
    it = Departement.objects.get(nom_service='Informatique')
    rh = Departement.objects.get(nom_service='Ressources Humaines')
    mkt = Departement.objects.get(nom_service='Marketing')
    
    # Create a new department
    com, _ = Departement.objects.get_or_create(nom_service='Commercial')

    extra_data = [
        ('Leroy', 'Thomas', 'Développeur', 3800, date(2023, 11, 10), 'Master Informatique', it, 'CDI'),
        ('Moreau', 'Camille', 'RH', 3000, date(2024, 2, 1), 'Master RH', rh, 'CDI'),
        ('Fournier', 'Julien', 'Développeur', 4200, date(2024, 1, 15), 'Master Data Science', it, 'CDI'),
        ('Girard', 'Alice', 'Autre', 2800, date(2023, 12, 1), 'Licence Communication', mkt, 'CDD'),
        ('Lefebvre', 'Nicolas', 'Commercial', 3500, date(2022, 5, 20), 'Master Vente', com, 'CDI'),
        ('Dubois', 'Emma', 'RH', 2400, date(2024, 3, 10), 'BTS Gestion', rh, 'CDD'),
        ('Rousseau', 'Antoine', 'Développeur', 3900, date(2021, 9, 15), 'Licence Pro Réseaux', it, 'CDI'),
        ('Lambert', 'Chloé', 'Autre', 3600, date(2023, 10, 5), 'Master Design', it, 'CDI'),
        ('Bonnet', 'Hugo', 'Autre', 4500, date(2020, 11, 1), 'Master Marketing', mkt, 'CDI'),
        ('Vincent', 'Léa', 'Commercial', 2600, date(2024, 4, 20), 'Licence Commerce', com, 'CDD'),
    ]

    for nom, prenom, poste, salaire, d_emb, diplome, dep, t_contrat in extra_data:
        e = Employe.objects.create(
            nom=nom, prenom=prenom, type_poste=poste,
            salaire=salaire, date_embauche=d_emb,
            dernier_diplome=diplome, departement=dep
        )
        Contrat.objects.create(employe=e, type_contrat=t_contrat)

    print(f"10 employés supplémentaires ajoutés avec succès !")

if __name__ == '__main__':
    seed_extra()
