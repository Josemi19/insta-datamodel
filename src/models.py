import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__= "usuario"
    id = Column(Integer, primary_key = True)

    seguidor = relationship("seguidor")
    seguidor_id = Column(Integer, ForeignKey("seguidor.id"))

    seguido = relationship("seguido")
    seguido_id = Column(Integer, ForeignKey("seguido.id"))

    post = relationship("post")
    post_id = Column(Integer, ForeignKey("post.id"))

    user = Column(String(50), nullable = False, unique = True)
    email = Column(String(50), nullable = False, unique = True)
    password = Column(String(20), nullable = False)
    fecha_sub = Column(Date, nullable = False)
    nombre = Column(String(50), nullable = False)
    apellido = Column(String(50), nullable = True)

class Seguidor(Base):
    __tablename__ = "seguidor"
    id = Column(Integer, primary_key = True)

class Seguido(Base):
    __tablename__ = "seguido"
    id = Column(Integer, primary_key = True)

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key = True)

    megusta = relationship("megusta")
    megusta_id = Column(Integer, ForeignKey("megusta.id"))

    comment = relationship("comment")
    comment_id = Column(Integer, ForeignKey("comment.id"))

    guardado = relationship("guardado")
    guardado_id = Column(Integer, ForeignKey("guardado.id"))

    caption = Column(String(100), nullable = True)
    media = Column(String(100), nullable = False)

class MeGusta(Base):
    __tablename__ = "megusta"
    id = Column(Integer, primary_key = True)

class Comentarios(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key = True)

    mensaje = Column(String(60))

class Guardado(Base):
    __tablename__ = "guardado"
    id = Column(Integer, primary_key = True)

    
    

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e