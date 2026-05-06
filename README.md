# 💼 HR-Manager

**HR-Manager** est une application web de gestion des ressources humaines développée avec Django. Elle permet de centraliser le suivi des employés, la gestion des contrats et le pilotage de la masse salariale à travers une interface moderne et intuitive.

---

## ✨ Fonctionnalités Principales

### 👨‍💼 Espace Administrateur (Staff)
- **Tableau de Bord Analytique** : Vue d'ensemble de l'effectif, de la masse salariale et des recrutements récents.
- **Gestion des Employés** : Création, modification et archivage des profils.
- **Filtres Avancés** : Recherche par nom et filtrage par poste.
- **Statistiques** : Répartition de la masse salariale par département.
- **Gestion des Services** : Organisation par départements avec responsables dédiés.

### 👤 Espace Employé
- **Profil Personnel** : Consultation des informations professionnelles et calcul automatique de l'ancienneté.
- **Mon Équipe** : Visualisation des collègues au sein du même département pour favoriser la cohésion.
- **Interface Simplifiée** : Accès restreint pour garantir la sécurité des données.

---

## 🛠️ Stack Technique

- **Framework** : [Django 4.2+](https://www.djangoproject.com/)
- **Base de données** : SQLite (par défaut)
- **Design** : Vanilla CSS (Variables, Flexbox, Grids)
- **Icônes** : FontAwesome

---

## 🚀 Installation & Utilisation

### 1. Cloner le projet
```bash
git clone https://github.com/Spoon007/HR-Manager.git
cd HR-Manager
```

### 2. Créer un environnement virtuel (optionnel)
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install django
```

### 4. Initialiser la base de données
```bash
python manage.py migrate
```

### 5. Peupler la base avec des données de test
```bash
python seed_db.py
```

### 6. Lancer le serveur
```bash
python manage.py runserver
```
L'application sera disponible sur `http://127.0.0.1:8000`.

---

## 📂 Structure du Projet

- `hr_app/` : Application principale (modèles, vues, templates).
- `hr_manager_project/` : Configuration globale du projet Django.
- `seed_db.py` : Script d'initialisation des données de test.
- `PROJET_PHASES.md` : Documentation détaillée des phases de développement.

---

## 📜 Licence
Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

---
*Développé avec ❤️ par Antigravity*