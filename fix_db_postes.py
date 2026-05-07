import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hr_manager_project.settings')
django.setup()

from hr_app.models import Employe

def fix_postes():
    mapping = {
        'Développeur Fullstack': 'Développeur',
        'Chargée de Recrutement': 'RH',
        'Analyste Data': 'Développeur',
        'Community Manager': 'Autre',
        'Commercial Senior': 'Commercial',
        'Assistante Administrative': 'RH',
        'Administrateur Systèmes': 'Développeur',
        'Designer UI/UX': 'Autre',
        'Chef de Projet Marketing': 'Autre',
        'Commerciale Junior': 'Commercial',
    }
    
    count = 0
    for old_poste, new_poste in mapping.items():
        updated = Employe.objects.filter(type_poste=old_poste).update(type_poste=new_poste)
        count += updated
        
    print(f"Correction terminée. {count} employés mis à jour.")

if __name__ == '__main__':
    fix_postes()
