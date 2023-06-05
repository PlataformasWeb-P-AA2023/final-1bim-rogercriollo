from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
from genera_tablas import  Provincia, Canton, Parroquia, Institucion

from configuracion import BaseDatos
#Conexión con SQlite
engine = create_engine(BaseDatos)

Session = sessionmaker(bind=engine)
session = Session()

archivo = pd.read_csv('./data/Listado-Instituciones-Educativas.csv', delimiter='|')
#Cantones insertar
#**********************************************
cantones = archivo[['Provincia', 'Código División Política Administrativa  Cantón', 'Cantón']]

print(cantones)

noRepetir = cantones.drop_duplicates()

print(noRepetir)

for index, row in noRepetir.iterrows():
    val1 = row['Provincia']
    val2 = row['Código División Política Administrativa  Cantón']
    val3 = row['Cantón']

    provincia1 = session.query(Provincia).filter_by(provincia=val1).one()

    print(provincia1)

    canton = Canton(cod=val2, canton=val3, provincia=provincia1)
    print(canton)
    session.add(canton)

session.commit()