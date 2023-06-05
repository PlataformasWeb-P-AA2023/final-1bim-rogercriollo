from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ , or_
from genera_tablas import Institucion, Parroquia, Provincia, Canton
from configuracion import BaseDatos

#Conexión con SQlite
engine = create_engine(BaseDatos)

Session = sessionmaker(bind=engine)



Session = sessionmaker(bind=engine)
session = Session()

consulta1 = session.query(Parroquia).select_from(Parroquia).join(Parroquia.institucion).filter(Institucion.jornada.like("%Matutina y Vespertina%")).distinct()

print("Las parroquias que tienen establecimientos únicamente en la jornada Matutina y Vespertina:\n")
for e in consulta1:
    print(e.cod, e.parroquia)
    print("----------------------------------\n")

print("------------------------------Fin de la  Consulta ---------------------------------------\n")

consulta2 = session.query(Canton).select_from(Canton).join(Canton.parroquia).join(Parroquia.institucion).filter(
    or_(Institucion.numStudents.like("%448%"),Institucion.numStudents.like("%450%"),
        Institucion.numStudents.like("%451%"),Institucion.numStudents.like("%454%"),
        Institucion.numStudents.like("%458%"),Institucion.numStudents.like("%459%"))).distinct()

print("Los cantones que tiene establecimientos como número de estudiantes tales como: 448, 450, 451, 454, 458, 459:\n")
for e in consulta2:
    print(e.cod, e.canton)
    print("----------------------------------\n")

print("------------------------------Fin de la  Consulta ---------------------------------------\n")

