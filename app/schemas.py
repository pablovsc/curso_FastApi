from pydantic import BaseModel
from typing import Optional
from datetime import datetime

#modelo usuarioi
class User(BaseModel):
    nombre:str
    username:str
    password:str
    telefono:Optional[int]
    creacion:datetime=datetime.now()
     
class Usuario_id(BaseModel ):
    id:int