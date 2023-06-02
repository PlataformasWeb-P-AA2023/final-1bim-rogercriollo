from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ , or_
from genera_tablas import Institucion, Parroquia, Provincia, Canton
from configuracion import BaseDatos

#Conexión con SQlite
engine = create_engine(BaseDatos)
Session = sessionmaker(bind=engine)

with Session() as session:
    print("/********************************* NUmero de estudiantes *****************************/")
    # Los establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores.
    inst = session.query(Institucion).filter(Institucion.numStudents>100).order_by(Institucion.numStudents).all()
    print(inst)


    print("/********************************* NUmero de Profesores *******************************/")
    # Los establecimientos ordenados por número de profesores; que tengan más de 100 profesores.
    inst = session.query(Institucion).filter(Institucion.numTeachers>100).order_by(Institucion.numTeachers).all()
    print(inst)
