-- 3.a : Total des quantités vendues par région
SELECT region, SUM(qte) AS total_qte
FROM ventes
GROUP BY region;

-- 3.b : Total des quantités vendues par produit
SELECT produit, SUM(qte) AS total_qte
FROM ventes
GROUP BY produit;

-- 3.c : Chiffre d'affaires par produit
SELECT produit, SUM(prix * qte) AS chiffre_affaires
FROM ventes
GROUP BY produit;
