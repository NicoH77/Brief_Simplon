import csv

fichier_csv = 'ventes.csv'
ventes_par_produit = {}

with open(fichier_csv, newline='', encoding='utf-8') as f:
    # lecture du fichier CSV
    données = csv.DictReader(f, delimiter=',', quotechar='"')
        # Parcours des lignes
    for ligne in données:
        # affichage de la ligne
        # print(ligne)
        
        produit = ligne["produit"]
        quantite = int(ligne["qte"])

        if produit in ventes_par_produit:
            ventes_par_produit[produit] += quantite
        else:
            ventes_par_produit[produit] = quantite

# Affichage des ventes par produit
print(ventes_par_produit)

# Produit le plus vendu
produit_le_plus_vendu = max(ventes_par_produit, key=ventes_par_produit.get)
quantite_la_plus_vendue = ventes_par_produit[produit_le_plus_vendu]
print(f"Le produit le plus vendu est '{produit_le_plus_vendu}' avec une quantité de {quantite_la_plus_vendue}.")

# Produit le moins vendu
produit_le_moins_vendu = min(ventes_par_produit, key=ventes_par_produit.get)
quantite_la_moins_vendue = ventes_par_produit[produit_le_moins_vendu]
print(f"Le produit le moins vendu est '{produit_le_moins_vendu}' avec une quantité de {quantite_la_moins_vendue}.")



