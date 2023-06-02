from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ , or_
from genera_tablas import Institucion, Parroquia, Provincia, Canton, TiposSostenimiento, Distrito
from configuracion import BaseDatos

#Conexión con SQlite
engine = create_engine(BaseDatos)

Session = sessionmaker(bind=engine)


with Session() as session:
        print("/***************************************** 40 profesores: Educación regular **********************************************/")
        # Los establecimientos ordenados por nombre de parroquia que tengan más de 40 profesores y la cadena "Educación regular" en tipo de educación.
        inst = session.query(Institucion).join(Parroquia).\
                filter(Institucion.num_doc > 40).order_by(Parroquia.parroquia).all()
        print(inst)

        print("/************************************ Distrito 11D04 *****************************************/")
        # Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D04.

        inst = session.query(Institucion).join(TiposSostenimiento).join(Parroquia).join(Canton).join(Distrito).\
                filter(Distrito.descripcion  == "07D05").order_by(TiposSostenimiento.descripcion).all()
        print(inst)