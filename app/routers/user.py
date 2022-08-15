from fastapi import APIRouter, Depends
from app.schemas import User,Usuario_id
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db import models

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

usuarios=[]

@router.get("/ruta1")
def ruta1():
    return{"mensaje":"hola"}

@router.get('/')
def obtener_usuario(db:Session = Depends(get_db)):
    data = db.query(models.User).all()
    print(data)
    return usuarios

@router.post("/")
def crear_usuario(user:User):
    usuario=user.dict()
    usuarios.append(usuario)
    return {"respuesta":"usuario creado"}

@router.post("/{user_id}")
def obtener_usuario(user_id:int):
    for user in usuarios:
        if(user["id"]==user_id):
            return{"usuario":user}
    return{"respuesta":"usuario no encontrado"}

@router.post("/obtener_usuario")
def obtener_usuario2(user_id:Usuario_id):
    for user in usuarios:
        if(user["id"]==user_id.id):
            return{"usuario":user}
    return{"respuesta":"usuario no encontrado"}

@router.delete('/{user_id}')
def eliminar_usuario(user_id:int):
    for index,user in enumerate(usuarios):
        if user["id"]==user_id:
            usuarios.pop(index)
            return{"respuesta":"usuario eliminado"}
    return{"respuesta":"usuario no encontrado"}
         
@router.put('/{user_id}')
def actualizar(user_id:int, updateUser:User):
    for index,user in enumerate(usuarios):
        if user["id"]==user_id:
            usuarios[index]["nombre"] = updateUser.dict()['nombre']
            return{"respuesta":"usuario actualizdo"}
    return{"respuesta":"usuario no encontrado"}