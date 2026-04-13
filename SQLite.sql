SELECT * FROM ventes;

-- Chiffre d'affaire total
select sum(prix*qte) from ventes;

-- ventes par produit
select produit, prix as "prix unitaire", sum(qte) as "quantité", sum(prix*qte) as "prix total" from ventes
group by produit;

-- ventes par région
select region, sum(qte) as "quantité", sum(prix*qte) as "prix total" from ventes
group by region;
