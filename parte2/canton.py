from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
from genera_tablas import  Provincia, Canton

from configuracion import BaseDatos
#Conexión con SQlite
engine = create_engine(BaseDatos)

Session = sessionmaker(bind=engine)
session = Session()

## cantones 

archivo = pd.read_csv('./data/Listado-Instituciones-Educativas.csv', delimiter='|')


cantones = archivo[[ 'Código División Política Administrativa  Cantón', 'Cantón','Provincia']]

print(cantones)

noRepetir = cantones.drop_duplicates()

print(noRepetir)

for index, row in noRepetir.iterrows():
    val2 = row['Código División Política Administrativa  Cantón']
    val1 = row['Cantón']

    val3 = row['Provincia']

    canton = session.query(canton).filter_by(provincia=val1).one()

    print(canton)

    canton = Canton(cod=val2, Canton=val3, id_provincia=canton)
    print(canton)
    session.add(canton)

session.commit()
