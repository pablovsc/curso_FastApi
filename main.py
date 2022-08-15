from fastapi import FastAPI
import uvicorn
from app.routers import user
from app.db.database import Base,engine

def create_table():
    Base.metadata.create_all(bind=engine)

create_table()

app = FastAPI()

app.include_router(user.router) 

if __name__=="__main__":
    uvicorn.run("main:app",port=8080, reload=True)  