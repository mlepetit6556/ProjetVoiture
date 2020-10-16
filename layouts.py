#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import numpy as np
from app import app
from dash.dependencies import Input, Output
from Figures import figRegUn, figMultiVar, figSVM

car_Data = pd.read_csv("carData.csv")

def layout(data, question):
    if question ==0:
        layout =html.Div([
            html.P(''),
            html.P('Je suis Data Scientist et souhaite acheter une voiture. Je dispose de données issues du site Web de voitures CarDekho contenant des informations sur une grande variété de voitures dont leur prix. Je souhaite utiliser ces données pour déterminer le prix exact pour une voiture spécifique et être certain de faire une bonne affaire. '),
            html.H6('Comment utiliser les données du site pour déterminer le prix à payer ?')
        ])
    if question ==1:
        layout =html.Div([
            html.P(''),
            html.P('On dispose des caractéristiques suivantes :'),
            html.P('Le modèle de la voiture'),
            html.P("L'année de fabrication de la voiture"),
            html.P('Le prix de vente de la voiture (Selling_Price)'),
            html.P('Le prix actuel de la voiture (Present_Price)'),
            html.P('Le nombre de kilomètres parcourus par la voiture'),
            html.P('Le type de carburant utilisé par la voiture'),
            html.P('Le type du vendeur (Professionnel, Particulier...)'),
            html.P('Le type de transmission de la voiture (Automatique, Manuel...)'),
            html.P("Le nombre d'anciens propriétaires de la voiture"),
            html.P(''),
            html.H6("Quelles grandeurs utiliser pour déterminer le prix d'une voiture spécifique?"),
            html.P(''),
            html.P("Nous allons tout d'abord essayer plusieurs modèles de régression linéaire en déterminant le prix de vente du véhicule à partir de l'année et comparer leurs performances puis nous mettrons en place un modèle plus élaboré prenant en compte le nombre de kilomètres parcourus par chaque voiture pour déterminer son prix. Ensuite, nous essaierons un modèle de SVM sur ce problème et analyserons les différences avec les premiers modèles que nous avons utilisés. Finalement, nous montrerons les limites du modèle en étudiant un cas pratique."),
        ])

    elif question == 2:

        layout = html.Div([
            dcc.Graph(figure=figRegUn),
            html.P("On cherche à déterminer le prix de vente d'après l'année de fabrication du véhicule."),
            html.P("Pour cela, on effectue plusieurs modèles de régression linéaire en utilisant les librairies Numpy, Scipy, Sklearn et en créant soi-même une classe LinearRegression."),
            html.P("On obtient sensiblement les mêmes résultats (erreur obtenue et droite de régression) avec les différentes méthodes."),
            html.P("En observant les résultats sur un graphique, on voit que pour une même année de fabrication, on obtient des prix de vente très différents (jusqu'à 200 fois plus important). Il semble donc judicieux de prendre en compte d'autres paramètres que l'année pour déterminer le prix de vente."),
            html.H6("Essayons maintenant une régression multivariée en prenant en compte l'année de fabrication et le nombre de kilomètres parcourus pour déterminer le prix de vente.")
        ])

    elif question ==3:
        layout = html.Div([
            dcc.Graph(figure=figMultiVar),
            html.P("On effectue une régression linéaire en prenant en compte l'année de fabrication et le nombre de kilomètres parcourus pour déterminer le prix de vente du véhicule."),
            html.P("Logiquement, on obtient une erreur moins importante que pour les autres modèles ; il y a moins de chances que 2 voitures aient les 3 mêmes coordonnées."),
            html.P("Cette représentation n'est malheureusement pas très visuelle et parlante. Pour avoir une version plus partante, vous trouverez ensuite un calculateur prédisant le prix d'un véhicule selon son année et son nombre de kilomètres.")
        ])

    elif question ==4:
        layout = html.Div([
            html.H1("Estimateur de prix"),
            html.H3("Choix de l'année"),
            dcc.Input(
                id='annee',
                type='number',
                value=2016
            ),
            html.H3("Nombre de kilomètres parcourus"),
            dcc.Input(
                id='kmdriven',
                type='number',
                value=100
            ),

            html.P("\n"),
            html.P("\n"),
            html.P(id="prix"),
            html.H6("Dans le cadre de notre modèle multivarié, ce calculateur permet donc à l'utilisateur de déterminer le juste prix d'un véhicule donné."),
            html.P("Ce calculateur a des limites car on remarque que plus le nombre de kilomètres est important, plus le prix est élevé ce qui est bien sûr contraire à la réalité.")
        ])
    elif question ==5:
        layout = html.Div([
            dcc.Graph(figure=figSVM),
            html.P("On effectue une régression linéaire en prenant en compte l'année de fabrication pour déterminer le prix de vente du véhicule en utilisant un modèle de SVM."),
            html.P("Par rapport aux premiers modèles utilisés, on observe une droite de régression différente et une erreur plus importante. Ceci est dû au fait que les modèles de régression dits classiques et le SVM n'utilisent pas la même d'optimisation pour calculer les coefficients de la droite."),
            html.P("Les premiers modèles de régression déterminent les coefficients de la droite de régression pour minimiser l'erreur totale du modèle. Cette erreur totale correspond à la somme de la différence au carré entre une prédiction et la valeur réelle."),
            html.P("Le SVM, quant à lui, cherche à minimiser la distance entre la droite de régression et les points. Il est donc normal que nous obtenions une erreur plus importante dans le cas du SVM.")
        ])
    elif question ==6:
        layout = html.Div([
            html.P("\n"),
            html.P("Étudions maitenant les limites de nos modèles monovarié et multivarié."),
            html.P("Il peut arriver qu'en utilisant notre modèle, une personne trouve votre voiture au meilleur prix mais que 3 jours plus tard, cette dernière tombe en panne."),
            html.H6("Quelles données manquaient-t-ils à l'acheteur pour prédire cette panne ?"),
            html.P("En considérant seulement l'année de fabrication du véhicule et le nombre de kilomètres parcourus par le véhicule, on ne peux pas déterminer réellement son état. En effet, un véhicule peut être récent et avoir peu de kilomètres au compteur mais avoir eu un accident : il ne sera donc pas en bon état. Au contraire, un véhicule ancien, ayant autant de kilomètres peut avoir été entretenu régulièrement par son propriétaire et être donc en meilleur état. "),
            html.P("Il faudrait donc mettre en place un système de notation de l'état des véhicules pour remédier à ce problème.")
        ])

    return(layout)

