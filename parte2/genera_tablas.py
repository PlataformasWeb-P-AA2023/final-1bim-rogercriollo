from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Table

from configuracion import BaseDatos

#Conexión con SQlite
engine = create_engine(BaseDatos)

Base = declarative_base()

class Institucion(Base):
    __tablename__ = 'institucion'

    id = Column(Integer, primary_key=True, autoincrement=True)
    codParroquia = Column(String(10), ForeignKey('parroquia.cod'))
    codDistrito = Column(String(250))

    amie = Column(String(10))
    nombreInstitucion = Column(String(250))
    sostenimiento = Column(String(50))
    tipoEducacion = Column(String(50))
    modalidad = Column(String(50))
    jornada = Column(String(50))
    acceso = Column(String(50))
    numStudents = Column(Integer)
    numTeachers = Column(Integer)

    parroquia = relationship("Parroquia", back_populates="institucion")

    def __repr__(self):
        return "Institucion: Código Distrito: %s - Código AMIE: %s - Nombre: %s - Sostenimiento: %s - Tipo de Educación: %s - Modalidad: %s - Jornada: %s - Acceso: %s - Número de Estudiantes: %d - Número de Docentes: %d" % (
                self.codDistrito, self.amie, self.nombreInstitucion, self.sostenimiento,
                self.tipoEducacion, self.modalidad, self.jornada,
                self.acceso, self.numStudents, self.numTeachers)
                
#  la tabla parroquia
class Parroquia(Base):
    __tablename__ = 'parroquia'
    cod = Column(String(10), primary_key=True)
    parroquia = Column(String(250))
    id_canton = Column(String(10), ForeignKey('canton.cod'))
    canton = relationship("Canton", back_populates="parroquia")
    institucion = relationship("Institucion", back_populates="parroquia")

    def __repr__(self):
                return "Parroquia: cod=%s parroquia=%s " % (
                          self.cod, 
                          self.parroquia)


#  la tabla canton
class Canton(Base):
    __tablename__ = 'canton'
    cod = Column(String(10), primary_key=True)
    canton = Column(String(250))
    id_provincia = Column(String(10), ForeignKey('provincia.cod'))
    provincia = relationship("Provincia", back_populates="canton")
    parroquia = relationship("Parroquia", back_populates="canton")

    def __repr__(self):
         return "Canton: cod: %s - canton: %s" % (
                self.cod, self.canton)


#  tabla Provincia
class Provincia(Base):
    __tablename__ = 'provincia'
    cod = Column(String(10), primary_key=True)
    provincia = Column(String(250))
    canton = relationship("Canton", back_populates="provincia")

    def __repr__(self):
            return "Provincia: cod=%s provincia=%s " % (
                          self.cod, 
                          self.provincia)

Base.metadata.create_all(engine)









