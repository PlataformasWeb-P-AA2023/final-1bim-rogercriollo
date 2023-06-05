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
