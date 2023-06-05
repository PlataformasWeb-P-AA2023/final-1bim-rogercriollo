from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ , or_
from genera_tablas import Institucion, Parroquia, Provincia, Canton
from configuracion import BaseDatos

#Conexión con SQlite
engine = create_engine(BaseDatos)

Session = sessionmaker(bind=engine)

session = Session()

consulta = session.query(Institucion).join(Institucion.parroquia).filter(
    and_(Institucion.modalidad.like("%Educación regular%"), Institucion.nombreInstitucion >= 40)).order_by(Parroquia.parroquia).all()

print("Los establecimientos ordenados por nombre de parroquia que tengan más de 40 profesores y la cadena Educación regular en tipo de educación:\n")
for institucion in consulta:
    print(institucion.nombreInstitucion, institucion.modalidad, institucion.numTeachers)
    print("----------------------------------\n")

print("------------------------------Fin de la  Consulta ---------------------------------------\n")

consulta2 = session.query(Institucion).filter(Institucion.codDistrito.like("%11D04%")).order_by(Institucion.sostenimiento).all()

print("Todos los establecimientos ordenados por sostenimiento y que tengan código de distrito 11D04:\n")
for institucion in consulta2:
    print(institucion.sostenimiento, institucion.nombreInstitucion, institucion.codDistrito)
    print("----------------------------------\n")

print("------------------------------Fin de la  Consulta ---------------------------------------\n")
