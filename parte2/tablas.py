
#  tabla tipo de educación
class TipoEducacion(Base):
    __tablename__ = 'tipos_educacion'
    id = Column(Integer, primary_key=True)
    descripcion = Column(String(100))
    institucion = relationship("Institucion", back_populates="tipos_educacion")
    
    def __repr__(self):
        return self.descripcion       

#  tabla Tipos de sostenimiento
class TiposSostenimiento(Base):
    __tablename__ = 'tipos_sostenimiento'
    id = Column(Integer, primary_key=True)
    descripcion = Column(String(100))
    institucion = relationship("Institucion", back_populates="tipos_sostenimiento")
    
    def __repr__(self):
        return self.descripcion

#  tabla Tipos de acceso
class Tipo_acceso(Base):
    __tablename__ = 'tipo_acceso'
    id = Column(Integer, primary_key=True)
    descripcion = Column(String(100))
    instituciones = relationship("Institucion", back_populates ="tipo_acceso")

    def __repr__(self):
        return self.descripcion