import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import numpy as np
from app import app
from dash.dependencies import Input, Output
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR

car_Data = pd.read_csv("carData.csv")

fit = np.polyfit(car_Data.Year, car_Data.Selling_Price, 1)
poly = np.poly1d(fit)
preds = poly(car_Data.Year)

figRegUn = {
                'data':[
                    go.Scatter(
                        x=car_Data.Year,
                        y=car_Data.Selling_Price,
                        mode='markers',
                        opacity=0.8,
                        marker={
                            'size': 15,
                            'line': {'width': 0.5, 'color': 'white'}
                        },
                        name='Données réelles'
                    ),
                    go.Scatter(
                        x=car_Data.Year,
                        y=preds,
                        mode='lines',
                        opacity=0.8,
                        marker={
                            'size': 15,
                            'line': {'width': 0.5, 'color': 'white'}
                        },
                        name='Données issues de la régression'
                    ),

                ],
                   'layout': go.Layout(
                       xaxis={'title': 'Year'},
                       yaxis={'title': 'Selling Price'},
                       margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                       legend={'x': 1.0, 'y': 0.3},
                       hovermode='closest'
                   ),
                }

model=LinearRegression()

years=car_Data['Year']
kms=car_Data['Kms_Driven']
x=[[years[i], kms[i]] for i in range(len(years))]
y=car_Data['Selling_Price']
model.fit(x, y)
preds=model.predict(x)

figMultiVar = {
                'data':[
                    go.Scatter3d(
                        x=car_Data.Year,
                        y=car_Data.Kms_Driven,
                        z=car_Data.Selling_Price,
                        mode='markers',
                        #opacity=0.8,
                        #marker={
                            #'size': 15,
                            #'line': {'width': 0.5, 'color': 'white'}
                        #},
                        name='Données réelles'
                    ),
                    go.Scatter3d(
                        x=car_Data.Year,
                        y=car_Data.Kms_Driven,
                        z=preds,
                        mode='markers',
                        #opacity=0.8,
                        #marker={
                            #'size': 15,
                            #'line': {'width': 0.5, 'color': 'white'}
                        #},
                        name='Données issues de la régression'
                    ),


                ],


                }

years=car_Data['Year']
x=[[year] for year in years]
y=car_Data['Selling_Price']

model=SVR(kernel='linear')
model.fit(x, y)
preds=model.predict(x)

figSVM = {
                'data':[
                    go.Scatter(
                        x=car_Data.Year,
                        y=car_Data.Selling_Price,
                        mode='markers',
                        opacity=0.8,
                        marker={
                            'size': 15,
                            'line': {'width': 0.5, 'color': 'white'}
                        },
                        name='Données réelles'
                    ),
                    go.Scatter(
                        x=car_Data.Year,
                        y=preds,
                        mode='lines',
                        opacity=0.8,
                        marker={
                            'size': 15,
                            'line': {'width': 0.5, 'color': 'white'}
                        },
                        name='Données issues de la régression'
                    ),


                ],


                }
