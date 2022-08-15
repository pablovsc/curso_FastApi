from app.db.database import Base
from sqlalchemy import Column,Integer,String, Boolean, DateTime
from datetime import datetime

"""
id:int
    nombre:str 
    telefono:Optional[str]
    creacion:datetime=datetime.now()
"""

class User(Base):
    __tablename__= "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    telefono = Column(Integer)
    creacion = Column(DateTime,default=datetime.now,onupdate=datetime.now)
    estado = Column(Boolean)