##Importations des librairies nécessaires

import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import sklearn
import scipy.optimize as op
from sklearn.svm import SVR

## QUESTION 1 : Récupération des données

car_data=pd.read_csv('carData.csv')

## QUESTION 2 : Exploration des données
print(car_data.head(10))
print(car_data.shape) #Taille du jeu de données
for col in car_data.columns: #Nom des colonnes
    print(col)

print(car_data.info()) #Informations basiques sur les données (type....)
print(car_data.describe()) #Informations statiques sur les données numériques(quartiles, moyennes...)
print(car_data.median()) #Médiane de chaque variable numérique

##On trace la distribution de chaque donnée numérique avec un histogramme

plt.figure(1)
plt.hist(car_data.Year)
plt.title('Année de construction de la voiture')
plt.show()

plt.figure(2)
plt.hist(car_data.Selling_Price)
plt.title('Selling Price de la voiture')
plt.show()

plt.figure(3)
plt.hist(car_data.Present_Price)
plt.title('Present Price de la voiture')
plt.show()

plt.figure(4)
plt.hist(car_data.Kms_Driven)
plt.title('Nombre de kilomètres parcourus par la voiture')
plt.show()

plt.figure(5)
plt.hist(car_data.Owner)
plt.title('Nombre de propriétaires de la voiture')
plt.show()

## QUESTION 4 : Visualisation des données avec Seaborn

sns.pairplot(car_data) #Visualisation de la corrélation des données ; cette visualisation s'affiche sur le navigateur

sns.catplot(x='Year', y='Selling_Price', data=car_data, hue='Fuel_Type')
plt.title('Prix de vente selon année pour différents carburants ')
plt.show()

sns.catplot(x='Fuel_Type', y='Selling_Price', data=car_data)
plt.title('Prix de vente selon carburant')
plt.show()

## QUESTION 5 : Régression linéaire

fig = px.scatter_matrix(car_data) #On regarde si les données de la base sont corrélées
fig.show()

#Régression linéaire avec librairie Numpy

x=car_data['Year']
y=car_data['Selling_Price']

fit = np.polyfit(x, y, 1)
poly = np.poly1d(fit)
pred=poly(x)

plt.plot(x, y, 'o')
plt.plot(x, pred, c='red')
plt.title('Régression linéaire obtenue avec Numpy')
plt.show()

#Régression linéaire avec librairie Scipy

slope, intercept, r_value, p_value, std_err = stats.linregress(car_data.Year, car_data.Selling_Price)
def predict(x):
    return slope * x + intercept
fitLine = predict(car_data.Year)
plt.plot(car_data.Year, car_data.Selling_Price,'o')
plt.plot(car_data.Year, fitLine, c='r')
plt.title('Regression linéaire obtenue avec Scipy')
plt.show()

#Régression linéaire avec librairie slkearn

model=sklearn.linear_model.LinearRegression()

years=car_data['Year']
x=[[year] for year in years]
y=car_data['Selling_Price']

model.fit(x, y)

plt.plot(x, model.predict(x), c='red')
plt.plot(x, y, 'o')
plt.title('Régression linéaire obtenue avec sklearn')
plt.show()

#Régression linéaire avec plusieurs variables d'entrée avec librairie sklearn

model=sklearn.linear_model.LinearRegression()

years=car_data['Year']
kms=car_data['Kms_Driven']
x=[[years[i], kms[i]] for i in range(len(years))]
y=car_data['Selling_Price']

model.fit(x, y)
print(model.score(x,y))

##QUESTION 6 : Création de ma propre classe LinearRegression

class LinearRegression :
    def __init__(self):
        self.a=0
        self.b=0
    def entrainement(self, x, y):
        def erreur(vec):
            erreur=0
            for i in range(len(x)):
                a=vec[0]
                b=vec[1]
                pred=a*x[i]+b
                erreur+=(y[i]-pred)**2
            return(erreur)

        [self.a, self.b] = op.fmin_cg(erreur, (0, 0))

    def prediction(self, x):
        list=[]
        for i in range(len(x)):
            pred=(self.a*x[i])+self.b
            list.append(pred)
        return (list)

x=car_data['Year']
y=car_data['Selling_Price']

model=LinearRegression()
model.entrainement(x, y)
preds= model.prediction(x)

plt.plot(x, preds, c='red')
plt.plot(x, y, 'o')
plt.title('Régression linéaire obtenue avec ma classe')
plt.show()


##QUESTION 7 : Régression linéaire  avec SVM

years=car_data['Year']
x=[[year] for year in years]
y=car_data['Selling_Price']

model=SVR(kernel='linear')
model.fit(x, y)
preds=model.predict(x)

plt.plot(x, y, 'o')
plt.plot(x, preds, c='red')
plt.title('Régression linéaire obtenue avec SVR')

plt.show()

