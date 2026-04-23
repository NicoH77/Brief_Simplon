-- Requêtes SQL pour analyse des ventes

-- vérification du jeu de données
SELECT * FROM ventes;

-- Chiffre d'affaire total
SELECT
  SUM(prix * qte) AS "Chiffre d'affaire"
FROM ventes;

-- ventes par produit
SELECT
  produit,
  prix AS "prix unitaire",
  SUM(qte) AS "quantité",
  SUM(prix * qte) AS "prix total"
FROM ventes
GROUP BY produit;

-- ventes par région
SELECT
  region,
  SUM(qte) AS "quantité",
  SUM(prix * qte) AS "prix total"
FROM ventes
GROUP BY region;
