from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
from genera_tablas import  Provincia
from configuracion import BaseDatos
#Conexión con SQlite
engine = create_engine(BaseDatos)

Session = sessionmaker(bind=engine)
session = Session()

archivo = pd.read_csv('./data/Listado-Instituciones-Educativas.csv', delimiter='|')

#Provincias insertar
#**********************************************
provincias = archivo[['Código División Política Administrativa Provincia', 'Provincia']]

print(provincias)

noRepetir = provincias.drop_duplicates()

print(noRepetir)

for index, row in noRepetir.iterrows():
    val1 = row['Código División Política Administrativa Provincia']
    val2 = row['Provincia']
    provincia = Provincia(cod=val1, provincia=val2)
    print(provincia)
    session.add(provincia)

session.commit()