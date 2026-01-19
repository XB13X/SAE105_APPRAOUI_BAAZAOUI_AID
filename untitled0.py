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
            valeur_brute = ligne[2]
            if valeur_brute != "":
                valeur_propre = valeur_brute.replace(',', '.')
                valeur_finale = float(valeur_propre)
                dico[date] = valeur_finale

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



data_taux = preparer_donnees(taux_couverture_eolien)
dates_taux = sorted(data_taux.keys())
valeurs_taux = [data_taux[d] for d in dates_taux]

plt.figure(figsize=(10, 5))
plt.plot(dates_taux, valeurs_taux, label="Taux de couverture moyen (%)")
plt.xticks(dates_taux[::12], rotation=45)
plt.title("Évolution du Taux de Couverture Éolien Mensuel en France")
plt.ylabel("Pourcentage (%)")
plt.xlabel("Années")
plt.grid()
plt.legend()
plt.show()

def calcul_stats(dico):
    date_min = min(dico, key=dico.get)
    date_max = max(dico, key=dico.get)
    valeur_min = dico[date_min]
    valeur_max = dico[date_max]
    moyenne = sum(dico.values()) / len(dico)
    return date_min, valeur_min, date_max, valeur_max, moyenne

# Éolien
dmin, vmin, dmax, vmax, moy = calcul_stats(data_eolien)
print("Éolien :")
print("  Minimum :", vmin, "TWh en", dmin)
print("  Maximum :", vmax, "TWh en", dmax)
print("  Moyenne :", moy, "TWh")
print()

# Hydraulique
dmin, vmin, dmax, vmax, moy = calcul_stats(data_hydro)
print("Hydraulique :")
print("  Minimum :", vmin, "TWh en", dmin)
print("  Maximum :", vmax, "TWh en", dmax)
print("  Moyenne :", moy, "TWh")
print()

# Nucléaire
dmin, vmin, dmax, vmax, moy = calcul_stats(data_nuc)
print("Nucléaire :")
print("  Minimum :", vmin, "TWh en", dmin)
print("  Maximum :", vmax, "TWh en", dmax)
print("  Moyenne :", moy, "TWh")
print()

# Thermique fossile
dmin, vmin, dmax, vmax, moy = calcul_stats(data_fossile)
print("Thermique fossile :")
print("  Minimum :", vmin, "TWh en", dmin)
print("  Maximum :", vmax, "TWh en", dmax)
print("  Moyenne :", moy, "TWh")
print()

# Thermique renouvelable
dmin, vmin, dmax, vmax, moy = calcul_stats(data_renouv)
print("Thermique renouvelable :")
print("  Minimum :", vmin, "TWh en", dmin)
print("  Maximum :", vmax, "TWh en", dmax)
print("  Moyenne :", moy, "TWh")
print()

# Solaire
dmin, vmin, dmax, vmax, moy = calcul_stats(data_solaire)
print("Solaire :")
print("  Minimum :", vmin, "TWh en", dmin)
print("  Maximum :", vmax, "TWh en", dmax)
print("  Moyenne :", moy, "TWh")
print()

# Taux de couverture éolien
dmin, vmin, dmax, vmax, moy = calcul_stats(data_taux)
print("Taux de couverture éolien :")
print("  Minimum :", vmin, "% en", dmin)
print("  Maximum :", vmax, "% en", dmax)
print("  Moyenne :", moy, "%")
print()
