import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

# Chifffre d'affaire
données["prix_total"]=données["prix"]*données["qte"]


groupé = données.groupby(["produit"])
# print(groupé.describe())

# Chiffre d'affaire moyen par produit
print(données[["produit","prix_total"]].groupby("produit").mean())
# Chiffre d'affaire médian par produit
print(données[["produit","prix_total"]].groupby("produit").median())

# Volume de ventes moyen par produit
print(données[["produit","qte"]].groupby("produit").mean())
# Volume des ventes médian par produit
print(données[["produit","qte"]].groupby("produit").median())

# Écart-type et variance du chiffre d'affaire par produit
print(données[["produit","prix_total"]].groupby("produit").std())
print(données[["produit","prix_total"]].groupby("produit").var())

# Graphique de la répartition des ventes par produit
figure_qte = px.pie(données, values='qte', names='produit', title='quantité vendue par produit')
figure_qte.write_html('ventes-par-produit.html')

# Graphique de la répartition du chiffre d'affaire par produit
figure_ca = px.pie(données, values='prix_total', names='produit', title='Chiffre d affaire par produit')
figure_ca.write_html('ca-par-produit.html')


print('ventes-par-produit.html généré avec succès !')
