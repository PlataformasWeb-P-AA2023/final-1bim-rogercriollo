from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ , or_
from genera_tablas import Institucion, Parroquia, Provincia, Canton
from configuracion import BaseDatos

#Conexión con SQlite
engine = create_engine(BaseDatos)
Session = sessionmaker(bind=engine)
session = Session()
consulta = session.query(Institucion).filter(Institucion.numTeachers > 100).order_by(Institucion.numStudents).all()

print("Los establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores:\n")
for institucion in consulta:
    print(institucion.nombreInstitucion, institucion.numStudents, institucion.numTeachers)
    print("----------------------------------\n")

print("------------------------------Fin Consulta ---------------------------------------\n")

consulta2 = session.query(Institucion).filter(Institucion.numTeachers > 100).order_by(Institucion.numTeachers).all()

print("Los establecimientos ordenados por número de profesores; que tengan más de 100 profesores:\n")
for institucion in consulta2:
    print(institucion.nombreInstitucion, institucion.numTeachers)
    print("----------------------------------\n")

print("------------------------------Fin Consulta ---------------------------------------\n")
