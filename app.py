import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')
figure.write_html('ventes-par-region.html')

fig2 = px.bar(données.groupby('produit', as_index=False).agg({'qte': 'sum'}),
              x='produit', y='qte', title='Ventes par produit')
fig2.write_html("ventes-par-produit.html")

données['ca'] = données['prix'] * données['qte']
fig3 = px.bar(données.groupby('produit', as_index=False).agg({'ca': 'sum'}),
              x='produit', y='ca', title="Chiffre d'affaires par produit")
fig3.write_html("chiffre-affaires-par-produit.html")

print('Tous les graphiques ont été générés avec succès !')