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

# Route pour ajouter un nouvel étudiant
@app.route('/ajouter', methods=['GET', 'POST'])
def ajouter():
    if request.method == 'POST':
        nom = request.form['nom']
        age = int(request.form['age'])
        id_etudiant = request.form['id_etudiant']
        ajouter_etudiant(nom, age, id_etudiant)
        return redirect('/etudiants')
    return render_template('add_student.html')

# Route pour ajouter une note à un étudiant
@app.route('/ajouter_note/<id_etudiant>', methods=['GET', 'POST'])
def ajouter_note(id_etudiant):
    etudiant = trouver_etudiant_par_id(id_etudiant)
    if not etudiant:
        return "Étudiant non trouvé"
    
    if request.method == 'POST':
        note = float(request.form['note'])
        ajouter_note_a_etudiant(id_etudiant, note)
        return redirect('/etudiants')
    
    return render_template('add_note.html', etudiant=etudiant)

# Route pour modifier les informations d'un étudiant
@app.route('/modifier/<id_etudiant>', methods=['GET', 'POST'])
def modifier(id_etudiant):
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
