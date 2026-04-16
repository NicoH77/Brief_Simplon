# Rapport d’exercice – Analyse des ventes

Cet exercice a pour objectif d’analyser un jeu de données de ventes à partir de requêtes SQL simples.

## 1. Import du jeu de données

Import du jeu données sur https://sqliteonline.com/.

Le jeu de données est un fichier CSV de 40 lignes dont 1 ligne d'entête, contenant notamment les champs suivants :

- `date`
- `produit`
- `prix`
- `qte`
- `region`

Le jeu de données contient les chiffres de ventes de produits du 01/01/2022 au 20/01/2022. Pour chaque produit, sont indiqués : la date de vente, la région de vente, le prix unitaire et la quantité vendue 

## 2. Vérification de l'import

La requête suivante permet de vérifier que les données ont été correctement importées :

```sql
-- Affichage de l'integralité de la table vente
SELECT * FROM ventes;
```

La requête suivante permet de vérifier que l'ensemble des lignes du fichier ont été importées

```sql
-- Nombre de lignes dans la table ventes
SELECT count(*) FROM ventes;
```


---

## 3. Analyse SQL

### a. Chiffre d'affaire total

Requête :
```sql
-- Calcul du chiffre d'affaire total
SELECT
  SUM(prix * qte) AS "Chiffre d'affaire"
FROM ventes;
```

Résultat :
| Chiffre d'affaire |
|-----------|
| 44825    |


### b. Ventes par produit

Requête :
```sql
-- Calcul des ventes par produit. On affiche pour chaque produit : son prix unitaire, la quantité vendue, et le prix total.
SELECT
  produit,
  prix AS "prix unitaire",
  SUM(qte) AS "quantité",
  SUM(prix * qte) AS "prix total"
FROM ventes
GROUP BY produit;
```

Résultat :
<img width="913" height="175" alt="image" src="https://github.com/user-attachments/assets/bfd4f87f-0b34-4cc2-98d8-eea2e558b2b3" />


### c. Ventes par région

```sql
-- Calcul des ventes par région. On affiche pour chaque région : la quantité de produits vendue, et le prix total.
SELECT
  region,
  SUM(qte) AS "quantité",
  SUM(prix * qte) AS "prix total"
FROM ventes
GROUP BY region;
```
Résultat :
<img width="878" height="122" alt="image" src="https://github.com/user-attachments/assets/326431e2-515d-4993-9e38-4f55de28f8be" />


Note : les requêtes sql sont également disponibles dans le fichier `SQLite.sql`


## 4. Démarrage du projet dans GitHub Codespaces

A partir de ce paragraphe, l'objectif est de poursuivre l'analyse du fichier de données 'ventes.csv' en utilissant du code python au lieu de SQL. Nous utiliserons en particulier les deux outils : pandas et plotly.

Cette étape correspond à l'instanciation de l'environnementde travail sur Codespace


## 5. Exploration du jeu de données avec Pandas

Les résultats indiqués dans ce paragraphe ont été produits à partir du script `app.py`.

* Chiffre d’affaires par produit :
** moyenne
** médiane

Volume des ventes par produit :
** moyenne
** médiane
** écart-type
** variance





## 6. Produit le plus et le moins vendu

L'objectif de cette partie est de créer un code Python natif permetant de trouver le produit le plus vendu et le moins vendu en nombre d’unités vendues, sans utiliser Pandas.

Ce code est disponible dans le script `app2.py`

Réultat de l'exécution du script :

<img width="950" height="92" alt="image" src="https://github.com/user-attachments/assets/5bc2eb13-a163-4635-8930-5b6148737a42" />


## 7. Graphiques Plotly

L'objectif de cette partie est de proposer 2 nouveaux graphiques en s'appuyant sur plotty 



### a. Ventes par produit

```python
# Graphique de la répartition des ventes par produit
figure_qte = px.pie(données, values='qte', names='produit', title='quantité vendue par produit')
figure_qte.write_html('ventes-par-produit.html')
```

<img width="1512" height="716" alt="newplot (1)" src="https://github.com/user-attachments/assets/7dd09758-760e-4d2f-a400-f551e5a400f5" />


### b. Chiffre d'affaire par produit

```python
# Graphique de la répartition du chiffre d'affaire par produit
figure_ca = px.pie(données, values='prix_total', names='produit', title='Chiffre d affaire par produit')
figure_ca.write_html('ca-par-produit.html')
```

<img width="1512" height="716" alt="newplot" src="https://github.com/user-attachments/assets/9dfac609-d6df-491b-912a-75e4d257f930" />




## 7. Synthèse




