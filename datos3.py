from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ , or_
from genera_tablas import Institucion, Parroquia, Provincia, Canton
from configuracion import BaseDatos

#Conexión con SQlite
engine = create_engine(BaseDatos)

Session = sessionmaker(bind=engine)

with Session() as session:
        print("/********************************************** 0 número de profesores, 5 profesores, 11, profesores ************************************************/")
        # Los cantones que tiene establecimientos con 0 número de profesores, 5 profesores, 11, profesores
        cant = session.query(Canton).join(Parroquia).join(Institucion).\
                filter(or_(Institucion.num_doc == 0, Institucion.num_doc == 5, Institucion.num_doc == 11)).all()
        print(cant)

        print("/**************************************** Parroquia Pindal *************************************/")
        # Los establecimientos que pertenecen a la parroquia Pindal con estudiantes mayores o iguales a 21
        cant = session.query(Institucion).join(Parroquia).\
                filter(Parroquia.parroquia == "PINDAL").filter(Institucion.num_est >= 21).all()
        print(cant)
