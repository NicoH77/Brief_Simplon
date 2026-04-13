# Rapport d’exercice – Analyse des ventes

## 1. Contexte

Cet exercice a pour objectif d’analyser un jeu de données de ventes à partir de requêtes SQL simples.
La table `ventes` contient notamment les champs suivants :

- `produit`
- `prix`
- `qte`
- `region`


---

## 3. Analyse SQL

### a. Chiffre d'affaire total

Requête :
```sql
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
SELECT
  region,
  SUM(qte) AS "quantité",
  SUM(prix * qte) AS "prix total"
FROM ventes
GROUP BY region;
```
Résultat :
<img width="878" height="122" alt="image" src="https://github.com/user-attachments/assets/326431e2-515d-4993-9e38-4f55de28f8be" />


## 3. Résultat code Python
Résultat du script : app2.py

<img width="950" height="92" alt="image" src="https://github.com/user-attachments/assets/5bc2eb13-a163-4635-8930-5b6148737a42" />


## 7. Graphiques Plotly
### a. Ventes par produit
<img width="1512" height="716" alt="newplot (1)" src="https://github.com/user-attachments/assets/7dd09758-760e-4d2f-a400-f551e5a400f5" />

### b. Chiffre d'affaire par produit
<img width="1512" height="716" alt="newplot" src="https://github.com/user-attachments/assets/9dfac609-d6df-491b-912a-75e4d257f930" />



