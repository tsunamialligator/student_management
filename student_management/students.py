# students.py

class Etudiant:
    def __init__(self, nom, age, id_etudiant):
        self.nom = nom
        self.age = age
        self.id_etudiant = id_etudiant
        self.notes = []

    def ajouter_note(self, note):
        self.notes.append(note)

    def calculer_moyenne(self):
        if len(self.notes) == 0:
            return 0
        return sum(self.notes) / len(self.notes)

    def modifier_infos(self, nouveau_nom, nouvel_age):
        self.nom = nouveau_nom
        self.age = nouvel_age

# Liste globale pour stocker les étudiants
etudiants = []

# Fonctions pour gérer les étudiants
def ajouter_etudiant(nom, age, id_etudiant):
    etudiant = Etudiant(nom, age, id_etudiant)
    etudiants.append(etudiant)

def obtenir_tous_les_etudiants():
    return etudiants

def trouver_etudiant_par_id(id_etudiant):
    for etudiant in etudiants:
        if etudiant.id_etudiant == id_etudiant:
            return etudiant
    return None

def supprimer_etudiant(id_etudiant):
    global etudiants
    etudiants = [etudiant for etudiant in etudiants if etudiant.id_etudiant != id_etudiant]
    
def ajouter_note_a_etudiant(id_etudiant, note):
    etudiant = trouver_etudiant_par_id(id_etudiant)
    if etudiant:
        etudiant.ajouter_note(note)

def modifier_infos_etudiant(id_etudiant, nouveau_nom, nouvel_age):
    etudiant = trouver_etudiant_par_id(id_etudiant)
    if etudiant:
        etudiant.modifier_infos(nouveau_nom, nouvel_age)