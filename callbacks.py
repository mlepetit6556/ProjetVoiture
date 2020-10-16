#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from dash.dependencies import Input, Output

from app import app
import pandas as pd
import plotly.graph_objs as go
from layouts import *
from sklearn.linear_model import LinearRegression

@app.callback(Output('url', 'pathname'),
              [Input('Mode', 'value'),
               ])
def display_page(mode):
    if mode == 0:
        return '/apps/Intro'
    elif mode ==1:
        return '/apps/Explication'
    elif mode ==2:
        return '/apps/ClasseUnique'
    elif mode ==3:
        return '/apps/MultiVar'
    elif mode ==4:
        return '/apps/Calculateur'
    elif mode ==5:
        return '/apps/SVM'
    elif mode ==6:
        return '/apps/Bonus'

@app.callback(
    Output('prix', 'children'),
    [Input('annee','value'),
     Input('kmdriven','value'),])
def calcul_prix(year,km):
    if year not in range(2006,2019):
        return "L'année doit être comprise entre 2006 et 2018"
    if km not in range(0,500000):
        return "Le kilométrage doit être compris entre 0 et 500000km"

    model = LinearRegression()
    years = car_Data['Year']
    kms = car_Data['Kms_Driven']
    x = [[years[i], kms[i]] for i in range(len(years))]
    y = car_Data['Selling_Price']
    model.fit(x, y)
    prix = model.predict([[year, km]])
    prix= float(prix)*1000
    return "La voiture est estimée à %.2f €"% prix
