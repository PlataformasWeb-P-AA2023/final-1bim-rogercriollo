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

#Parroquias insertar
#**********************************************
parroquias = archivo[['Cantón', 'Código División Política Administrativa  Parroquia', 'Parroquia']]

print(parroquias)

noRepetir = parroquias.drop_duplicates()

print(noRepetir)

for index, row in noRepetir.iterrows():
    val1 = row['Cantón']
    val2 = row['Código División Política Administrativa  Parroquia']
    val3 = row['Parroquia']

    cantonObj = session.query(Canton).filter_by(canton=val1).one()

    print(cantonObj)

    parroquia = Parroquia(cod=val2, parroquia=val3, canton=cantonObj)
    print(parroquia)
    session.add(parroquia)

session.commit()