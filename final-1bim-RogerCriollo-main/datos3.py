from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ , or_
from genera_tablas import Institucion, Parroquia, Provincia, Canton
from configuracion import BaseDatos

#Conexión con SQlite
engine = create_engine(BaseDatos)

Session = sessionmaker(bind=engine)

session = Session()
# Query to find cantones with establishments having 0, 5, or 11 teachers
consulta = session.query(Canton).select_from(Canton).join(Canton.parroquia).join(Parroquia.institucion).filter(
    or_(Institucion.numTeachers.like("%0%"), Institucion.numTeachers.like("%5%"),
        Institucion.numTeachers.like("%11%"))).distinct()

print("Los cantones que tienen establecimientos con 0, 5 o 11 profesores:\n")
for canton in consulta:
    print(canton.cod, canton.canton)
    print("----------------------------------\n")

print("------------------------------Fin de la  Consulta ---------------------------------------\n")




# Query to find establishments in the parroquia "Pindal" with at least 21 students
consulta2 = session.query(Institucion).join(Institucion.parroquia).filter(
    and_(Parroquia.parroquia.like("%Pindal%"), Institucion.numStudents >= 21)).all()

print("Los establecimientos que pertenecen a la parroquia Pindal con estudiantes mayores o iguales a 21:\n")
for institucion in consulta2:
    print(institucion.nombreInstitucion, institucion.numStudents)
    print("----------------------------------\n")

print("------------------------------Fin Consulta ---------------------------------------\n")
