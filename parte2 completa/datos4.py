from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ , or_
from genera_tablas import Institucion, Parroquia, Provincia, Canton
from configuracion import BaseDatos

#Conexión con SQlite
engine = create_engine(BaseDatos)

Session = sessionmaker(bind=engine)


with Session() as session:
        print("/***************************************** 40 profesores: Educación regular **********************************************/")
        # Los establecimientos ordenados por nombre de parroquia que tengan más de 40 profesores y la cadena "Educación regular" en tipo de educación.
        inst = session.query(Institucion).join(Parroquia).\
                filter(Institucion.numTeachers > 40).order_by(Parroquia.parroquia).all()
        print(inst)

      


        print("/************************************ Distrito 11D04 *****************************************/")
        # Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D04.

        Distrito = session.query(Institucion).filter(Institucion.codDistrito.like("%11D04%")).order_by(Institucion.sostenimiento).all()

print(" Institucion ordenados  por  distrito 11D04:\n")
for e in Distrito:
    print (e.sostenimiento, e.id, e.codDistrito)


