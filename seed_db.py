import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hr_manager_project.settings')
django.setup()

from hr_app.models import Employe, Departement, Contrat
from django.contrib.auth.models import User

def seed():
    # Clean up
    Contrat.objects.all().delete()
    Employe.objects.all().delete()
    Departement.objects.all().delete()
    
    # Create Departments
    it = Departement.objects.create(nom_service='Informatique')
    rh = Departement.objects.create(nom_service='Ressources Humaines')
    mkt = Departement.objects.create(nom_service='Marketing')
    com = Departement.objects.create(nom_service='Commercial')

    # Create Employees
    e1 = Employe.objects.create(
        nom='Dupont', prenom='Jean', type_poste='Directeur RH', 
        salaire=4500, date_embauche=date(2020, 1, 10), 
        dernier_diplome='Master RH', departement=rh
    )
    e2 = Employe.objects.create(
        nom='Martin', prenom='Sophie', type_poste='Développeur', 
        salaire=3500, date_embauche=date(2022, 3, 15), 
        dernier_diplome='Ingénieur Info', departement=it
    )
    e3 = Employe.objects.create(
        nom='Petit', prenom='Marie', type_poste='Chef de Projet IT', 
        salaire=4000, date_embauche=date(2026, 4, 15), 
        dernier_diplome='Master Management', departement=it
    )
    e4 = Employe.objects.create(
        nom='Bernard', prenom='Lucas', type_poste='RH', 
        salaire=3200, date_embauche=date(2021, 11, 5), 
        dernier_diplome='Licence RH', departement=rh
    )

    # Extra Employees
    extra_data = [
        ('Leroy', 'Thomas', 'Développeur Fullstack', 3800, date(2023, 11, 10), 'Master Informatique', it, 'CDI'),
        ('Moreau', 'Camille', 'Chargée de Recrutement', 3000, date(2024, 2, 1), 'Master RH', rh, 'CDI'),
        ('Fournier', 'Julien', 'Analyste Data', 4200, date(2024, 1, 15), 'Master Data Science', it, 'CDI'),
        ('Girard', 'Alice', 'Community Manager', 2800, date(2023, 12, 1), 'Licence Communication', mkt, 'CDD'),
        ('Lefebvre', 'Nicolas', 'Commercial Senior', 3500, date(2022, 5, 20), 'Master Vente', com, 'CDI'),
        ('Dubois', 'Emma', 'Assistante Administrative', 2400, date(2024, 3, 10), 'BTS Gestion', rh, 'CDD'),
        ('Rousseau', 'Antoine', 'Administrateur Systèmes', 3900, date(2021, 9, 15), 'Licence Pro Réseaux', it, 'CDI'),
        ('Lambert', 'Chloé', 'Designer UI/UX', 3600, date(2023, 10, 5), 'Master Design', it, 'CDI'),
        ('Bonnet', 'Hugo', 'Chef de Projet Marketing', 4500, date(2020, 11, 1), 'Master Marketing', mkt, 'CDI'),
        ('Vincent', 'Léa', 'Commerciale Junior', 2600, date(2024, 4, 20), 'Licence Commerce', com, 'CDD'),
    ]

    for nom, prenom, poste, salaire, d_emb, diplome, dep, t_contrat in extra_data:
        emp = Employe.objects.create(
            nom=nom, prenom=prenom, type_poste=poste,
            salaire=salaire, date_embauche=d_emb,
            dernier_diplome=diplome, departement=dep
        )
        Contrat.objects.create(employe=emp, type_contrat=t_contrat)

    # Set Responsables
    it.responsable = e3
    it.save()
    rh.responsable = e1
    rh.save()

    # Create Contrats for first 4
    Contrat.objects.create(employe=e1, type_contrat='CDI')
    Contrat.objects.create(employe=e2, type_contrat='CDI')
    Contrat.objects.create(employe=e3, type_contrat='CDI')
    Contrat.objects.create(employe=e4, type_contrat='CDI')

    # Ensure accounts exist
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    
    # Update smartin
    u_smartin = User.objects.filter(username='smartin').first()
    if u_smartin:
        u_smartin.first_name = 'Sophie'
        u_smartin.last_name = 'Martin'
        u_smartin.save()

    print("Base de données initialisée avec succès avec 14 employés !")

if __name__ == '__main__':
    seed()
