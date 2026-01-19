📊 Projet SAE105 - Analyse de la production éolienne en France
📋 Description
Analyse comparative de la production d'énergie éolienne en France entre 2010 et 2025, basée sur les données ouvertes de RTE (Réseau de Transport d'Électricité). Ce projet étudie l'évolution temporelle de l'éolien et sa place dans le mix énergétique français.
👥 Équipe
[Nom Prénom 1] - Développement et analyse
[Nom Prénom 2] - Visualisation et rédaction
Groupe de TP : [Votre Groupe]
📅 Contexte académique
Module : SAE105 - Analyse de données
Sujet choisi : Projet n°19 - Étudier l'importance de la production d'énergie d'origine éolienne
Date limite de rendu : 19/01/2026 à 17h30
🎯 Objectifs
Analyser l'évolution mensuelle de la production éolienne (2010-2025)
Comparer l'éolien avec les autres filières énergétiques
Calculer et visualiser le taux de couverture éolien
Extraire des statistiques clés pour chaque filière
📁 Structure du projet
projet-eolien-sae105/
│
├── 📊 data/ # Données sources RTE
│ ├── evolution_de_la_production_eolienne.csv
│ ├── evolution_de_la_production_nucleaire.csv
│ ├── evolution_de_la_production_delectricite_hydraulique.csv
│ ├── evolution_de_la_production_solaire_photovoltaique.csv
│ ├── evolution_de_la_production_thermique_fossile.csv
│ ├── evolution_de_la_production_thermique_renouvelable_et_dechets.csv
│ └── Taux_de_couverture_eolien.csv
│
├── 📝 src/ # Code source
│ └── analyse_eolien.py # Script principal (version finale)
│
├── 📈 outputs/ # Résultats générés
│ ├── graphs/ # Graphiques (générés à l'exécution)
│ └── stats.txt # Statistiques exportées
│
├── 📄 docs/ # Documentation
│ ├── compte_rendu.pdf # Compte-rendu final
│ └── README.md # Ce fichier
│
├── 📋 requirements.txt # Dépendances Python
└── .gitignore # Configuration Git

🚀 Installation et utilisation
pip install -r requirements.txt
python src/analyse_eolien.py
1. Chargement des données
ouverture(evolution_production_eolien, "fichier.csv", ";")
2. Nettoyage et préparation
data_eolien = preparer_donnees(evolution_production_eolien)
3. Visualisations comparatives
tracer_comparaison(data_eolien, data_nuc, "Nucléaire", "Éolien vs Nucléaire")
4. Analyse statistique
dmin, vmin, dmax, vmax, moy = calcul_stats(data_eolien)

📊 Fichiers de données utilisés
Fichier	Description	Période	Unité
evolution_de_la_production_eolienne.csv				Production mensuelle éolienne		2010-2025	TWh
evolution_de_la_production_nucleaire.csv			Production nucléaire			2010-2025	TWh
evolution_de_la_production_delectricite_hydraulique.csv		Production hydraulique			2010-2025	TWh
evolution_de_la_production_solaire_photovoltaique.csv		Production solaire			2010-2025	TWh
evolution_de_la_production_thermique_fossile.csv		Production thermique fossile		2010-2025	TWh
evolution_de_production_thermique_renouvelable_et_dechets.csv   Production thermique renouvelable	2010-2025	TWh
Taux_de_couverture_eolien.csv					Taux de couverture mensuel		2014-2025	%

Initialisation
git init
git add .
git commit -m "Initial commit - Projet éolien SAE105"
Organisation des commits
git add src/analyse_eolien.py
git commit -m "feat: implémentation des fonctions principales"
git commit -m "docs: ajout des commentaires et documentation"
git commit -m "fix: correction gestion des dates manquantes"
Connexion à GitHub
git remote add origin [URL_GITHUB]
git push -u origin main

#test manuel
Vérification du nombre de données
print(f"Données éoliennes : {len(data_eolien)} points")
print(f"Données nucléaires : {len(data_nuc)} points")
Doit retourner ~180 points (15 ans × 12 mois)
