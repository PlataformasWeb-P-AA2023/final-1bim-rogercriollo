from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ 
from genera_tablas import Institucion, Parroquia, Provincia, Canton
from configuracion import BaseDatos

#Conexión con SQlite
engine = create_engine(BaseDatos)


Session = sessionmaker(bind=engine)

with Session() as session:
    print("\n/**************************************** Parroquia Pindal *************************************/\n")
    # Los establecimientos que pertenecen a la parroquia Pindal con estudiantes mayores o iguales a 21
    cant = session.query(Institucion).join(Parroquia).\
                filter(Parroquia.parroquia == "PINDAL").filter(Institucion.numStudents >= 21).all()
    for a in cant:
        print(f"Institución: {a.nombreInstitucion} - Estudiantes: {a.numStudents}")
    
    print("\n/******** Canton Portovelo ********/\n")
    # Todos los establecimientos del cantón de Portovelo.

    ints = session.query(Institucion).join(Parroquia).join(Canton).\
            filter(Canton.canton == "PORTOVELO").all()
    for e in ints:
        print(e.nombreInstitucion)

    print("\n/********************************* Jornada: Matutina y Vespertina *********************************/\n")
    # Las parroquias que tienen establecimientos únicamente en la jornada "Matutina y Vespertina"
    inst = session.query(Institucion).filter(Institucion.jornada=="Matutina y Vespertina" ).all()
    for i in inst:
        print(f"Institución: {i.nombreInstitucion} - Jornada: {i.jornada}")
        