from ast import For
from code import interact
from email.policy import default
from enum import unique
from tkinter import CASCADE
from app.db.database import Base
from sqlalchemy import Column,Integer,String, Boolean, DateTime
from datetime import datetime
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__= "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    username = Column(String, unique=True)
    password = Column(String)
    telefono = Column(Integer, unique=True)
    creacion = Column(DateTime,default=datetime.now,onupdate=datetime.now)
    estado = Column(Boolean,default=False)
    venta = relationship("Venta",backref="user", cascade="delete,merge")

class Venta(Base): 
    __tablename__ = "venta"
    id = Column(Integer, primary_key=True, autoincrement=True)
    User_id =  Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    Venta = Column(Integer)
    Venta_Producto = Column(Integer)