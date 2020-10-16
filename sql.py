import csv
import sqlite3

con = sqlite3.connect("car_data.db")
cur = con.cursor()

cur.execute('''CREATE TABLE cardata(
  Car_Name      VARCHAR(25) NOT NULL 
  ,Year          INTEGER  NOT NULL
  ,Selling_Price NUMERIC(5,2) NOT NULL
  ,Present_Price NUMERIC(5,3) NOT NULL
  ,Kms_Driven    INTEGER  NOT NULL
  ,Fuel_Type     VARCHAR(6) NOT NULL
  ,Seller_Type   VARCHAR(10) NOT NULL
  ,Transmission  VARCHAR(9) NOT NULL
  ,Owner         INTEGER  NOT NULL
);''')


with open('carData.csv', 'r') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['Car_Name'], i['Year'], i['Selling_Price'], i['Present_Price'], i['Kms_Driven'], i['Fuel_Type'], i['Seller_Type'], i['Transmission'], i['Owner']) for i in dr]

cur.executemany("INSERT INTO cardata (Car_Name, Year, Selling_Price, Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission,Owner) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
con.commit()

l = cur.execute('SELECT * FROM cardata WHERE Kms_Driven > 100000').fetchall()
print(l)