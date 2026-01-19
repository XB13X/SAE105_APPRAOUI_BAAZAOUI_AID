import csv
import matplotlib.pyplot as plt
from datetime import datetime

def ouverture(l, fic, deli):
    with open(fic, newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=deli)
        next(reader)  # supprimer l’en-tête
        for row in reader:
            if row:
                l.append(row)

# Listes
evolution_production_eolien = []
evolution_production_hydrolique = []
evolution_production_nucleaire = []
evolution_production_thermiques_fossiles = []
evolution_production_thermiques_renouvable = []
evolution_production_solaire = []
taux_couverture_eolien = []

# Ouverture des fichiers
ouverture(evolution_production_eolien, "evolution_de_la_production_eolienne.csv", ";")
ouverture(evolution_production_hydrolique, "evolution_de_la_production_delectricite_hydraulique.csv", ";")
ouverture(evolution_production_nucleaire, "evolution_de_la_production_nucleaire.csv", ";")
ouverture(evolution_production_thermiques_fossiles, "evolution_de_la_production_thermique_fossile.csv", ";")
ouverture(evolution_production_thermiques_renouvable, "evolution_de_la_production_thermique_renouvelable_et_dechets.csv", ";")
ouverture(evolution_production_solaire, "evolution_de_la_production_solaire_photovoltaique.csv", ";")
ouverture(taux_couverture_eolien, "Taux_de_couverture_eolien.csv", ";")

def preparer_donnees(liste_donnees):
    dico = {}

    for ligne in liste_donnees:
        if len(ligne) >= 3:
            date = ligne[0]
            valeur = ligne[2]

            if valeur != "":
                valeur = float(valeur.replace(',', '.'))
                dico[date] = valeur

    return dico

# Dictionnaires
data_eolien = preparer_donnees(evolution_production_eolien)
data_hydro = preparer_donnees(evolution_production_hydrolique)
data_nuc = preparer_donnees(evolution_production_nucleaire)
data_fossile = preparer_donnees(evolution_production_thermiques_fossiles)
data_renouv = preparer_donnees(evolution_production_thermiques_renouvable)
data_solaire = preparer_donnees(evolution_production_solaire)

def tracer_comparaison(base_data, compare_data, label_compare, titre, unite="TWh"):
    dates = []

    for d in base_data:
        if d in compare_data:
            dates.append(d)

    dates.sort()

    y_base = []
    y_compare = []

    for d in dates:
        y_base.append(base_data[d])
        y_compare.append(compare_data[d])

    plt.figure()
    plt.plot(dates, y_base, label="Éolien")
    plt.plot(dates, y_compare, label=label_compare)

    plt.xticks(dates[::12], rotation=45)
    plt.ylabel(unite)
    plt.title(titre)
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()


# Comparaisons
tracer_comparaison(data_eolien, data_nuc, "Nucléaire", "Éolien vs Nucléaire")
tracer_comparaison(data_eolien, data_hydro, "Hydraulique", "Éolien vs Hydraulique")
tracer_comparaison(data_eolien, data_solaire, "Solaire", "Éolien vs Solaire")
tracer_comparaison(data_eolien, data_fossile, "Thermique Fossile", "Éolien vs Thermique Fossile")
tracer_comparaison(data_eolien, data_renouv, "Thermique Renouvelable", "Éolien vs Thermique Renouvelable")