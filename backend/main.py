from fastapi import FastAPI
from db import conectar_db
app = FastAPI()


@app.get("/")
def home():
    return {"status": "ok", "mensaje": "API funcionando 🚀"}