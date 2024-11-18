# app.py
from flask import Flask, render_template, request, redirect
from students import (ajouter_etudiant, obtenir_tous_les_etudiants, 
                      trouver_etudiant_par_id, supprimer_etudiant, 
                      ajouter_note_a_etudiant, modifier_infos_etudiant)

app = Flask(__name__)

# Route d'accueil
@app.route('/')
def index():
    return render_template('index.html')

# Route pour afficher tous les étudiants
@app.route('/etudiants')
def afficher_etudiants():
    etudiants = obtenir_tous_les_etudiants()
    return render_template('student_list.html', etudiants=etudiants)

# Fonction pour vérifier si l'ID existe déjà
def id_existe_deja(id_etudiant):
    etudiants = obtenir_tous_les_etudiants()
    for etudiant in etudiants:
        if etudiant.id_etudiant == id_etudiant:
            return True
    return False

# Route pour ajouter un nouvel étudiant
@app.route('/ajouter', methods=['GET', 'POST'])
def ajouter():
    if request.method == 'POST':
        nom = request.form['nom']
        age = int(request.form['age'])
        id_etudiant = request.form['id_etudiant']

        # Vérifier si l'ID existe déjà
        if id_existe_deja(id_etudiant):
            # Si l'ID existe déjà, afficher un message d'erreur
            message = "Cet identifiant est déjà utilisé. Veuillez en choisir un autre."
            return render_template('add_student.html', message=message)

        # Si l'ID est unique, ajouter l'étudiant
        ajouter_etudiant(nom, age, id_etudiant)
        return redirect('/etudiants')

    return render_template('add_student.html')

# Route pour afficher la page de sélection pour ajouter une note
@app.route('/note', methods=['GET', 'POST'])
def afficher_note():
    etudiants = obtenir_tous_les_etudiants()

    if request.method == 'POST':
        id_etudiant = request.form['id_etudiant']
        note = float(request.form['note'])

        # Vérifier que la note est entre 0 et 20
        if note < 0 or note > 20:
            return render_template('note.html', etudiants=etudiants, message="La note doit être comprise entre 0 et 20.")

        ajouter_note_a_etudiant(id_etudiant, note)

        # Rester sur la même page après l'ajout de la note
        return render_template('note.html', etudiants=etudiants, message="Note ajoutée avec succès !")

    return render_template('note.html', etudiants=etudiants)


# Route pour afficher la page de modification avec la liste déroulante
@app.route('/modifier')
def afficher_modifier():
    etudiants = obtenir_tous_les_etudiants()
    return render_template('modifier.html', etudiants=etudiants)

# Route pour modifier les informations d'un étudiant (après sélection)
@app.route('/modifier_etudiant', methods=['GET', 'POST'])
def modifier_etudiant():
    id_etudiant = request.args.get('id_etudiant')
    etudiant = trouver_etudiant_par_id(id_etudiant)
    
    if not etudiant:
        return "Étudiant non trouvé"

    if request.method == 'POST':
        nouveau_nom = request.form['nom']
        nouvel_age = int(request.form['age'])
        modifier_infos_etudiant(id_etudiant, nouveau_nom, nouvel_age)
        return redirect('/etudiants')

    return render_template('edit_student.html', etudiant=etudiant)

# Route pour supprimer un étudiant
@app.route('/supprimer/<id_etudiant>')
def supprimer(id_etudiant):
    supprimer_etudiant(id_etudiant)
    return redirect('/etudiants')

# Exécution de l'application
if __name__ == '__main__':
    app.run(debug=True)
