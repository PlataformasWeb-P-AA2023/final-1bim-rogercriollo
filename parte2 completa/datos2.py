from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ , or_
from genera_tablas import Institucion, Parroquia, Provincia, Canton
from configuracion import BaseDatos

#Conexión con SQlite
engine = create_engine(BaseDatos)

Session = sessionmaker(bind=engine)


with Session() as session:
    print("/********************************* Jornada: Matutina y Vespertina *********************************/")
    # Las parroquias que tienen establecimientos únicamente en la jornada "Matutina y Vespertina"
    inst = session.query(Institucion).filter(Institucion.jornada=="Matutina y Vespertina" ).all()

    for i in inst:
        print(f"Institución: {i} - Jornada: {i.jornada}")


    print("/********************************** Numero Estudiantes: 448, 450, 451, 454, 458, 459 *************************************/")
    # Los cantones que tiene establecimientos como número de estudiantes tales como: 448, 450, 451, 454, 458, 459
    cant = session.query(Canton).join(Parroquia).join(Institucion).\
            filter(or_(Institucion.numStudents == 448, Institucion.numStudents == 450, Institucion.numStudents == 451, Institucion.numStudents == 454, Institucion.numStudents == 458, Institucion.numStudents == 459)).all()
    print(cant)
