from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ 
from genera_tablas import Institucion, Parroquia, Provincia, Canton
from configuracion import BaseDatos

engine = create_engine(BaseDatos, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

consulta1 = session.query(Institucion).join(Parroquia).filter(Parroquia.cod == 110553).all()

print("Todos los establecimientos que pertenecen al Código División Política Administrativa Parroquia con valor 110553:\n")
for e in consulta1:
    print(e.id, e.nombreInstitucion,e.parroquia.parroquia,e.parroquia.canton.canton ,e.parroquia.canton.provincia.provincia)
    print("----------------------------------\n")

print("------------------------------Fin de la  Consulta ---------------------------------------\n")


consulta2 = session.query(Institucion).select_from(Institucion).join(Parroquia, Institucion.parroquia).join(
    Canton, Parroquia.canton).join(Provincia, Canton.provincia).filter(Provincia.provincia.like("%EL ORO%")).all()

print("Todas las Institucion de la provincia del Oro:\n")
for e in consulta2:
    print(e.id, e.nombreInstitucion)
    print("----------------------------------\n")

print("------------------------------Fin de la  Consulta ---------------------------------------\n")




consulta3 = session.query(Institucion).select_from(Institucion).join(Parroquia, Institucion.parroquia).join(
    Canton, Parroquia.canton).filter(Canton.canton.like("%Portovelo%")).all()

print("Todas las  Institucion del cantón de Portovelo:\n")
for e in consulta3:
    print(e.id, e.nombreInstitucion)
    print("----------------------------------\n")

print("------------------------------Fin de la  Consulta ---------------------------------------\n")




consulta4 = session.query(Institucion).select_from(Institucion).join(Parroquia, Institucion.parroquia).join(
    Canton, Parroquia.canton).filter(Canton.canton.like("%Zamora%")).all()

print("Todos las Institucion del cantón de Zamora:\n")
for e in consulta4:
    print(e.id, e.nombreInstitucion)
    print("----------------------------------\n")

print("------------------------------Fin de la  Consulta ---------------------------------------\n")








