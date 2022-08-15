from pydantic import BaseModel
from typing import Optional
from datetime import datetime

#modelo usuarioi
class User(BaseModel):
    id:int
    nombre:str
    telefono:Optional[str]
    creacion:datetime=datetime.now()
     
class Usuario_id(BaseModel ):
    id:int