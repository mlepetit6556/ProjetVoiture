#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

from app import app
from app import server
from layouts import *
import callbacks

car_Data = pd.read_csv("carData.csv")

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),

    html.H6("Choisissez la partie du problème à afficher"),
    dcc.RadioItems(
        options=[
            {'label': 'Introduction', 'value': 0},
            {'label': 'Explication du problème et des variables', 'value': 1},
            {'label': 'Régression linéaire à une classe', 'value': 2},
            {'label': 'Régression linéaire multivariée', 'value': 3},
            {'label': 'Calculateur de prix', 'value': 4},
            {'label': 'SVM', 'value': 5},
            {'label': 'Limites de notre modèle', 'value': 6},
        ],
        value=0,
        labelStyle={'display': 'inline-block'},
        id='Mode'
    ),

    html.Div(id='page-content')

])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/Intro':
        return layout(car_Data, 0)
    elif pathname == '/apps/Explication':
        return layout(car_Data, 1)
    elif pathname == '/apps/ClasseUnique':
        return layout(car_Data, 2)
    elif pathname == '/apps/MultiVar':
        return layout(car_Data, 3)
    elif pathname == '/apps/Calculateur':
        return layout(car_Data, 4)
    elif pathname == '/apps/SVM':
        return layout(car_Data, 5)
    elif pathname == '/apps/Bonus':
        return layout(car_Data, 6)
    else :
        return "Rajouter /apps/Intro à la fin de l'URL pour commencer la présentation"

if __name__ == '__main__':
    app.run_server(debug=True)

