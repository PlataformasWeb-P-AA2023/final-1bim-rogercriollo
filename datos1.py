from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ 
from genera_tablas import Institucion, Parroquia, Provincia, Canton
from configuracion import BaseDatos

#Conexión con SQlite
engine = create_engine(BaseDatos)


Session = sessionmaker(bind=engine)

with Session() as session:
    print("/*********************** COdigo: 110553 ********************/")
    # Todos los establecimientos que pertenecen al Código División Política Administrativa Parroquia con valor 110553
    inst = session.query(Institucion).filter(Institucion.id_parroquia==110553 ).all()
    print(inst)


    print("/*********************** Provincia ********************/")
    # Todos los establecimientos de la provincia del Oro

    inst = session.query(Institucion).join(Parroquia).join(Canton).join(Provincia).\
            filter(Provincia.provincia == "EL ORO").all()
    print(inst)
        
    print("/*********************** Canton Portovelo *********************/")
    # Todos los establecimientos del cantón de Portovelo.

    ints = session.query(Institucion).join(Parroquia).join(Canton).\
            filter(Canton.canton == "PORTOVELO").all()
    print(inst)
        
    print("/*********************** Canton Zamora *********************/")
    # Todos los establecimientos del cantón de Zamora.
    inst = session.query(Institucion).join(Parroquia).join(Canton).filter(Canton.canton == "ZAMORA").all()
    print(inst)