from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Table

from configuracion import BaseDatos

#Conexión con SQlite
engine = create_engine(BaseDatos)

Base = declarative_base()

# Modelo para crear la tabla distrito
class Distrito(Base):
    __tablename__ = 'distrito'
    id = Column(Integer, primary_key=True)
    descripcion = Column(String(100))
    canton = relationship("Canton", back_populates="distrito")

    def __repr__(self):
        return self.descripcion

#  tabla Provincia
class Provincia(Base):
    __tablename__ = 'provincia'
    cod = Column(Integer, primary_key=True)
    provincia = Column(String(250))
    canton = relationship("Canton", back_populates="provincia")

    def __repr__(self):
        return self.provincia

#  la tabla canton
class Canton(Base):
    __tablename__ = 'canton'
    cod = Column(Integer, primary_key=True)
    canton = Column(String(250))
    id_provincia = Column(Integer, ForeignKey('provincia.cod'))
    id_distrito = Column(Integer, ForeignKey('distrito.id'))
    provincia = relationship("Provincia", back_populates="canton")
    distrito = relationship("Distrito", back_populates="canton")
    parroquia = relationship("Parroquia", back_populates="canton")

    def __repr__(self):
        return self.canton

#  la tabla parroquia
class Parroquia(Base):
    __tablename__ = 'parroquia'
    cod = Column(Integer, primary_key=True)
    parroquia = Column(String(250))
    id_canton = Column(Integer, ForeignKey('canton.cod'))
    canton = relationship("Canton", back_populates="parroquia")
    institucion = relationship("Institucion", back_populates="parroquia")

    def __repr__(self):
        return self.parroquia



class Institucion(Base):
    __tablename__ = 'institucion'
    cod = Column(String(20), primary_key=True)
    nombre = Column(String(550))
    num_est = Column(Integer)
    num_doc = Column(Integer)
    modalidad = Column(String(300))
    jornada = Column(String(300))
    id_parroquia = Column(Integer, ForeignKey('parroquia.cod'))
    id_acceso = Column(Integer, ForeignKey('tipo_acceso.id'))
    id_sostenimiento = Column(Integer, ForeignKey('tipos_sostenimiento.id'))
    id_tipo_educacion = Column(Integer, ForeignKey('tipos_educacion.id'))
    tipo_acceso = relationship("Tipo_acceso", back_populates="instituciones")
    tipos_sostenimiento = relationship("TiposSostenimiento", back_populates="institucion")
    tipos_educacion = relationship("TipoEducacion", back_populates="institucion")
    parroquia = relationship("Parroquia", back_populates="institucion")
    

    def __repr__(self):
        return self.nombre


Base.metadata.create_all(engine)









