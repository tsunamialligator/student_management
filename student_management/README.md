# Application de Gestion des Étudiants avec Flask

Ce projet est une application web simple permettant de gérer les étudiants. Elle est développée avec le framework Flask en Python et permet d'ajouter de nouveaux étudiants, d'afficher la liste des étudiants, de gérer leurs notes, de modifier leurs informations, et de supprimer des étudiants. 

## Fonctionnalités

1. **Ajouter un étudiant** : 
   - Permet d'ajouter un étudiant en saisissant son nom, son âge, et son numéro d'identification.

2. **Afficher la liste des étudiants** : 
   - Affiche une liste de tous les étudiants avec leurs informations de base : nom, âge, numéro d'identification.

3. **Ajouter une note à un étudiant** : 
   - Permet d'ajouter une note pour un étudiant sélectionné. Les notes sont stockées sous forme de liste.

4. **Calculer la moyenne des notes** : 
   - Affiche la moyenne des notes de chaque étudiant.

5. **Modifier les informations d'un étudiant** : 
   - Permet de modifier le nom ou l'âge d'un étudiant.

6. **Supprimer un étudiant** : 
   - Supprime un étudiant de la liste en fonction de son numéro d'identification.

## Structure du Projet

Le projet est structuré de la manière suivante :
student_management/ 
├── app.py 
├── students.py 
├── static/ 
│ ├── styles.css
├── templates/
│ ├── index.html 
│ ├── student_list.html 
│ ├── add_student.html 
│ ├── edit_student.html 
│ └── add_note.html

- **app.py** : Fichier principal pour démarrer l'application Flask.
- **students.py** : Contient la classe `Etudiant` pour gérer la logique des étudiants.
- **static/styles.css** : Fichier CSS pour styliser l'interface.
- **templates/** : Dossier contenant les fichiers HTML pour l'interface utilisateur.

## Installation et Exécution

### Prérequis

- **Python** (version recommandée : 3.x)
- **Flask** (version recommandée : 2.x)

### Étapes d'installation

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/tsunamialligator/student_management.git
   cd student_management
