from fastapi import FastAPI, Depends
from dotenv import load_dotenvi
import os
from sqlalchemy import text
from sqlalchemy.orm import Session

#importação da configuração inicial do banco de daods
from core.database import get_db

#carrega variaveis do ambiente
load_dotenv()
app = FastAPI(
    title=os.getenv("APP_NAME"),
    version=os.getenv("APP_VERSION"),
)
@app.get("/")
def read_root():
    return{"message": "Bem-vindo à API Psilua"}

@app.get("/test-db")
def test_database_connection(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"Status": "sucess", "message": "Conexão com Banco de daDOS OK"}
    except Exception as error:
        return{"Status": "error", "message": f"Falha na conexão: {error}"}
    
    