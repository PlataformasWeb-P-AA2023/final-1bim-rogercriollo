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

#Instituciones insertar
#**********************************************
archivo = pd.read_csv('./data/Listado-Instituciones-Educativas.csv', delimiter='|')

establecimientos = archivo[['Código División Política Administrativa  Parroquia',\
                            'Código de Distrito', 'Nombre de la Institución Educativa',\
                            'Código AMIE', 'Sostenimiento', 'Tipo de Educación',\
                            'Modalidad', 'Jornada','Acceso (terrestre/ aéreo/fluvial)',\
                            'Número de estudiantes', 'Número de docentes']]

print(establecimientos)

noRepetir = establecimientos.drop_duplicates()

print(noRepetir)

for index, row in noRepetir.iterrows():
    val1 = row['Código División Política Administrativa  Parroquia']
    val2 = row['Código de Distrito']
    val3 = row['Nombre de la Institución Educativa']
    val4 = row['Código AMIE']
    val5 = row['Sostenimiento']
    val6 = row['Tipo de Educación']
    val7 = row['Modalidad']
    val8 = row['Jornada']
    val9 = row['Acceso (terrestre/ aéreo/fluvial)']
    val10 = row['Número de estudiantes']
    val11 = row['Número de docentes']

    parroquia1 = session.query(Parroquia).filter_by(cod=val1).one()

    print(parroquia1)

    establecimiento = Institucion(codParroquia=val1, codDistrito=val2, amie=val4,
                                      nombreInstitucion=val3, sostenimiento=val5, tipoEducacion=val6,
                                      modalidad=val7, jornada=val8, acceso=val9,
                                      numStudents =val10, numTeachers=val11,
                                      parroquia=parroquia1)

    print(establecimiento)
    session.add(establecimiento)


session.commit()


